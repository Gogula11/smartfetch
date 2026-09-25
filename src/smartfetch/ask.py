"""Ollama API client: query(data_dict, modelname) → response text.
Handles server availability checking and model interaction."""

import requests, os, subprocess, time

base = os.environ.get("OLLAMA_HOST", "http://localhost:11434/")

def _gpu_line(data_dict):
    gpus = data_dict.get("GPUs")
    if gpus:
        parts = []
        for g in gpus:
            if not g.get("GPU"):
                continue
            if g.get("VRAM Total") is None:
                parts.append(f"{g['GPU']} (shared system RAM)")
            else:
                parts.append(f"{g['GPU']} ({g['VRAM Used']}GB used / {g['VRAM Total']}GB)")
        total = sum(g.get("VRAM Total") or 0 for g in gpus)
        return f"GPUs: {'; '.join(parts)} — {total}GB discrete VRAM total"
    name, used, total = data_dict["GPU"], data_dict["VRAM Used"], data_dict["VRAM Total"]
    if not name:
        return "GPU: no discrete GPU reported"
    return f"GPU: {name} — VRAM: {used}GB used / {total}GB total"

def query(data_dict, modelname):
    """Sends hardware data payload to local Ollama instance and returns health verdict."""
    cpu = data_dict["CPU%"]
    ram_percent = data_dict["RAM%"]
    ram_used = data_dict["RAM Used"]
    ram_total = data_dict["RAM Total"]
    disk_percent = data_dict["Disk%"]
    disk_used = data_dict["Disk Used"]
    disk_total = data_dict["Disk Total"]
    battery = data_dict["Battery %"]
    os_type = data_dict["OS Type"]
    cpu_name = data_dict["CPU"]
    cpu_arch = data_dict["CPU Arch"]
    cpu_count = data_dict["CPU Count"]
    curr_cpu_freq = data_dict["Curr_CPU_Freq"]
    boost_cpu_freq = data_dict["Boost_CPU_Freq"]
    gpu_line = _gpu_line(data_dict)
    prompt = f"""
    PC: {os_type}.
    CPU: {cpu_name} ({cpu_arch}), {cpu_count} threads — {cpu}% in use at {curr_cpu_freq}GHz, boost up to {boost_cpu_freq}GHz.
    RAM: {ram_percent}% in use ({ram_used}GB of {ram_total}GB),
    {gpu_line},
    Disk: {disk_percent}% full ({disk_used}GB of {disk_total}GB).
    Battery: {battery}% charged.
    Using ONLY these values, reply in exactly five sentences (make sure to refer tot he names of the cpu and gpu too):
    (1) verdict on CPU load — judge the percentage, and treat a low GHz at idle as normal power saving, not a fault
    (2) verdict on memory pressure
    (3) verdict on disk usage
    (4) is it good for heavy load like professional works or games etc — reason from CPU threads, boost clock and  The GPU's VRAM together
    (5) one concrete improvement or 'no action needed'

    Judge each value against typical healthy ranges.
    Refer to the actual numbers. Do not mention anything that is not in the list."""

    if not server_up():
        subprocess.Popen(["ollama","serve"], start_new_session = True, stdout = subprocess.DEVNULL, stderr = subprocess.DEVNULL)
        for attempt in range(10):
            time.sleep(0.5)
            if server_up():
                break
        else:
            raise RuntimeError("Server not reachable or bootable")

    url = base + "api/generate"
    payload = {"model": modelname,"prompt": prompt, "stream": False, "options": {"num_predict": 280 , "temperature": 0.3}}
    res = requests.post(url,json=payload, timeout = 60)
    text = res.json()["response"]
    return text

def server_up():
    """Checks if Ollama server responds at configured endpoint."""
    try:
        requests.get(base + "api/version", timeout=2)
        return True
    except requests.exceptions.RequestException:
            return False

def model_loaded(modelname):
    """Checks if specific model is currently loaded in Ollama VRAM."""
    try:
        resp = requests.get(base + "api/ps", timeout=2)
        model_list = resp.json()

        for models in model_list["models"]:
            if models["name"].startswith(modelname):
                return True
        return False

    except Exception:
        return False



if __name__ == "__main__":

    data_dict = {"OS Type": "Linux", "CPU": "Intel i9", "CPU Arch": "x86_64",
    "CPU Count": 20, "Curr_CPU_Freq": 0.74, "Boost_CPU_Freq": 4.48,
    "CPU%": 12.5, "RAM%": 40.0, "RAM Used": 6.4, "RAM Total": 16.0,
    "GPU": "NVIDIA RTX 3070 Ti", "VRAM Used": 0.5, "VRAM Total": 8.0,
    "GPUs": [{"GPU": "NVIDIA RTX 3070 Ti", "VRAM Used": 0.5, "VRAM Total": 8.0},
             {"GPU": "AMD RX 7900 XTX", "VRAM Used": 1.0, "VRAM Total": 24.0}],
    "Disk%": 40.0, "Disk Used": 100.0, "Disk Total": 250.0, "Battery %": 96.74}
    modelname= "qwen2.5:1.5b"
    print(query(data_dict,modelname))
