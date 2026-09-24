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
    gpu = _safe(get_gpu_info) or {"GPU": None, "VRAM Used": None, "VRAM Total": None}

    specs = {"OS": os_name, "OS ID": os_id, "OS Type": os_type, "PC Name" :pc_name, "Battery %" : battery,
    "CPU" : cpu_name, "CPU Arch": cpu_arch, "CPU%": cpu_usage, "CPU Count": cpu_count, "Curr_CPU_Freq": curr_cpu_freq, 
    "Boost_CPU_Freq": boost_cpu_freq, "RAM Used": used_mem, "RAM Total": total_mem, "RAM%": mem.percent, 
    "Disk Used": used_disk, "Disk Total": total_disk, "Disk%": disk.percent if disk else None, "Boot Time" : boot_time,
    "GPU": gpu["GPU"], "VRAM Used": gpu["VRAM Used"], "VRAM Total": gpu["VRAM Total"]}
    return specs


def get_gpu_info():
    """Queries NVIDIA GPU name and VRAM stats via nvidia-smi CLI."""
    res = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.used,memory.total","--format=csv,noheader,nounits"], capture_output= True, text= True)
    parts = res.stdout.strip().split(",")
    gpu_name = parts[0].strip()
    
    vram_used = round((int(parts[1].strip()) / 1024),2)
    vram_total = round((int(parts[2].strip()) / 1024),2)
    return {"GPU": gpu_name, "VRAM Used": vram_used, "VRAM Total": vram_total}

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
