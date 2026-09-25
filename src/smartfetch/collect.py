"""Hardware reader: snapshot() returns 19+ key dict.
None-tolerant contract: every metric returns real value or None, never raises.
OS sources: /etc/os-release, nvidia-smi, psutil, platform."""

import psutil, json, datetime, platform, subprocess

def snapshot():
    """Collects all hardware specs into a single 19+ key dictionary."""
    #CPU stuff
    cpu_name = get_cpu_info()
    cpu_arch = platform.machine()
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    freq = _safe(psutil.cpu_freq)
    curr_cpu_freq = round(freq.current / 1000, 2) if freq else None
    boost_cpu_freq = round(freq.max / 1000, 2) if freq else None

    #RAM
    mem = psutil.virtual_memory()
    total_mem = round((mem.total / 1024**3),2)
    used_mem = round((mem.used/ 1024**3),2)

    #STORAGE
    disk = _safe(psutil.disk_usage, "/") or _safe(psutil.disk_usage, "C:\\")
    used_disk = round(disk.used / 1024**3, 2) if disk else None
    total_disk = round(disk.total / 1024**3, 2) if disk else None
    
    #battery
    b = _safe(psutil.sensors_battery)
    battery = round(b.percent, 2) if b else None

    #others
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    
    #system platform info
    os_name = get_os_name()
    os_type = platform.system()
    pc_name = platform.node()
    os_id = get_os_id()

    #GPU
    gpus = _safe(get_gpu_info) or []
    first = gpus[0] if gpus else {"GPU": None, "VRAM Used": None, "VRAM Total": None}

    specs = {"OS": os_name, "OS ID": os_id, "OS Type": os_type, "PC Name" :pc_name, "Battery %" : battery,
    "CPU" : cpu_name, "CPU Arch": cpu_arch, "CPU%": cpu_usage, "CPU Count": cpu_count, "Curr_CPU_Freq": curr_cpu_freq,
    "Boost_CPU_Freq": boost_cpu_freq, "RAM Used": used_mem, "RAM Total": total_mem, "RAM%": mem.percent,
    "Disk Used": used_disk, "Disk Total": total_disk, "Disk%": disk.percent if disk else None, "Boot Time" : boot_time,
    "GPU": first["GPU"], "VRAM Used": first["VRAM Used"], "VRAM Total": first["VRAM Total"], "GPUs": gpus}
    return specs


def get_gpu_info():
    """Queries all GPUs via smi ladder plus lspci fallback. Returns list, empty if none."""
    gpus = []
    for probe in (_nvidia_info, _rocm_info, _intel_info):
        try:
            found = probe() or []
            gpus.extend([g for g in found if g.get("GPU")])
        except Exception:
            continue
    try:
        for pci in _lspci_info() or []:
            if not any(_same_card(pci["GPU"], g["GPU"]) for g in gpus if not g.get("_matched")):
                gpus.append(pci)
            else:
                for g in gpus:
                    if not g.get("_matched") and _same_card(pci["GPU"], g["GPU"]):
                        g["_matched"] = True
                        break
    except Exception:
        pass
    for g in gpus:
        g.pop("_matched", None)
    return gpus

_FILLER = {"corporation", "graphics", "compatible", "controller", "vga", "display", "device", "intel", "nvidia", "amd", "advanced", "micro", "devices"}

def _tokens(name):
    return {t for t in "".join(c.lower() if c.isalnum() else " " for c in name).split() if len(t) > 2 and t not in _FILLER}

def _same_card(a, b):
    if not a or not b:
        return False
    ta, tb = _tokens(a), _tokens(b)
    return len(ta & tb) >= 2

def _lspci_info():
    res = subprocess.run(["lspci"], capture_output=True, text=True, timeout=5)
    res.check_returncode()
    out = []
    for line in res.stdout.splitlines():
        low = line.lower()
        if "vga" not in low and "display" not in low and "3d controller" not in low:
            continue
        name = line.split(": ", 1)[1].strip() if ": " in line else line.strip()
        if name:
            out.append({"GPU": name, "VRAM Used": None, "VRAM Total": None})
    return out

def _nvidia_info():
    res = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.used,memory.total","--format=csv,noheader,nounits"], capture_output= True, text= True, timeout=5)
    res.check_returncode()
    out = []
    for line in res.stdout.strip().splitlines():
        if not line.strip():
            continue
        parts = line.split(",")
        out.append({"GPU": parts[0].strip(),
                    "VRAM Used": round(int(parts[1].strip()) / 1024, 2),
                    "VRAM Total": round(int(parts[2].strip()) / 1024, 2)})
    return out

def _rocm_info():
    res = subprocess.run(["rocm-smi", "--showproductname", "--showmeminfo", "vram", "--csv"], capture_output=True, text=True, timeout=5)
    res.check_returncode()
    lines = [l for l in res.stdout.strip().splitlines() if l.strip()]
    rows = lines[1:] if len(lines) > 1 and not lines[0][0].isdigit() and "card" in lines[0].lower() else lines
    out = []
    for row in rows:
        cols = [c.strip().strip('"') for c in row.split(",")]
        if len(cols) < 3:
            continue
        name = cols[0]
        total_b, used_b = int(float(cols[1])), int(float(cols[2]))
        out.append({"GPU": name, "VRAM Used": round(used_b / 1024**3, 2), "VRAM Total": round(total_b / 1024**3, 2)})
    return out

def _intel_info():
    res = subprocess.run(["xpu-smi", "discovery", "--dump", "1,5,18"], capture_output=True, text=True, timeout=5)
    res.check_returncode()
    out, cur = [], {}
    for line in res.stdout.splitlines():
        line = line.strip()
        if line.lower().startswith("device"):
            if cur.get("GPU"):
                out.append({"GPU": cur["GPU"], "VRAM Used": cur.get("VRAM Used"), "VRAM Total": cur.get("VRAM Total")})
            cur = {}
        elif line.lower().startswith("device name") or line.lower().startswith("product"):
            cur["GPU"] = line.split(":", 1)[1].strip() if ":" in line else line
        elif "memory" in line.lower() and ":" in line:
            nums = [n for n in line.replace(",", " ").split() if n.replace(".", "").isdigit()]
            if len(nums) >= 2:
                cur["VRAM Used"] = round(float(nums[0]) / 1024, 2)
                cur["VRAM Total"] = round(float(nums[1]) / 1024, 2)
    if cur.get("GPU"):
        out.append({"GPU": cur["GPU"], "VRAM Used": cur.get("VRAM Used"), "VRAM Total": cur.get("VRAM Total")})
    return out

def get_cpu_info():
    """Resolves CPU model string via platform or /proc/cpuinfo fallback."""
    if platform.processor():
        return platform.processor()

    try:
        with open('/proc/cpuinfo') as f:
            for line in f:
                if 'model name' in line:
                    return line.split(':',1)[1].strip()
    except Exception:
        pass
    return f"Unknown {platform.system()} CPU"

def get_os_name():
    """Resolves human-readable OS name, handling macOS and Linux releases."""
    os_type = platform.system()
    if os_type == 'Darwin':
        ver = _safe(platform.mac_ver)
        if ver and ver[0]:
            return f"macOS {ver[0]}"
        return "macOS"
        
    if os_type == 'Linux':
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        return line.split('=',1)[1].strip().strip('"')
        except Exception:
            pass
    return os_type

def get_os_id():
    """Resolves lowercase ID slug for ASCII logo lookup."""
    os_type = platform.system()
    if os_type == 'Linux':
        try:
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith("ID="):
                        return line.split('=',1)[1].strip().strip('"')
        
        except Exception:
            pass

    return {"Darwin": "macos", "Windows": "windows"}.get(os_type, os_type.lower())

def _safe(fn,*args):
    """EAFP wrapper: executes fn(*args), returns None on any exception."""
    try:
        return fn(*args)
    except Exception:
        return None

if  __name__ == "__main__":
    print(json.dumps(snapshot(), indent=2))
