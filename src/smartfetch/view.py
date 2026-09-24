"""Terminal UI: render(data_dict, ai_string) → rich panels.
Staged rendering via render_stats() and render_ai()."""

from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from smartfetch.logo import LOGOS

console = Console()

def render_stats(data_dict):
    """Renders ASCII logo and Hardware Stats panels side-by-side."""
    pc_name = data_dict["PC Name"]
    os_name = data_dict["OS"]
    os_type = data_dict["OS Type"]
    cpu_name = data_dict["CPU"]
    cpu_arch = data_dict["CPU Arch"]
    cpu = data_dict["CPU%"]
    cpu_count = data_dict["CPU Count"]
    curr_cpu_freq = data_dict["Curr_CPU_Freq"]
    boost_cpu_freq = data_dict["Boost_CPU_Freq"]
    ram_percent = data_dict["RAM%"]
    ram_used = data_dict["RAM Used"]
    ram_total = data_dict["RAM Total"]
    vram_used = data_dict["VRAM Used"]
    vram_total = data_dict["VRAM Total"]
    gpu_name = data_dict["GPU"]
    disk_percent = data_dict["Disk%"]
    disk_used = data_dict["Disk Used"]
    disk_total = data_dict["Disk Total"]
    boot_time = data_dict["Boot Time"]
    battery = data_dict["Battery %"]

    lines = [f"{pc_name} — {os_name} ({os_type})", ""]
    lines.append(f"CPU:   {cpu_name}")
    lines.append(f"Arch:  {cpu_arch} — {cpu_count} threads")
    if curr_cpu_freq is not None or boost_cpu_freq is not None:
        lines.append(f"Load:  {cpu}% @ {curr_cpu_freq}GHz, boost {boost_cpu_freq}GHz")
    else:
        lines.append(f"Load:  {cpu}%")
    if gpu_name is not None:
        lines.append(f"GPU:   {gpu_name}")
    if vram_used is not None or vram_total is not None:
        lines.append(f"VRAM:  {vram_used} / {vram_total}GB")
    lines.append(f"RAM:   {ram_used} / {ram_total}GB ({ram_percent}%)")
    if disk_used is not None or disk_total is not None or disk_percent is not None:
        lines.append(f"Disk:  {disk_used} / {disk_total}GB ({disk_percent}%)")
    lines.append(f"Boot:  {boot_time}")
    if battery is not None:
        lines.append(f"Power: {battery}%")
    stats_string = "\n".join(lines)
    logo = LOGOS.get(data_dict.get("OS ID", "linux"), LOGOS["linux"])
    for i, col in [("1", "cyan"), ("2", "green"), ("3", "black"), ("4", "blue"), ("5", "magenta"), ("6", "yellow")]:
        logo = logo.replace(f"${i}", f"[{col}]")
    try:
        from rich.text import Text
        logo_content = Text.from_markup(logo)
    except Exception:
        logo_content = logo
    logo_panel = Panel(logo_content, title= os_name, subtitle= "SmartFetch by Sohan Gogula", border_style="#00A3B1")
    panel1 = Panel(stats_string, title = "Hardware Stats", subtitle= "SmartFetch by Sohan Gogula", border_style="#FF6F61")
    console.print(Columns([logo_panel, panel1]))


def render_ai(ai_summary_string):
    """Renders AI Diagnosis summary panel below stats."""
    panel2 = Panel(ai_summary_string, title = "Ai Diagnosis", subtitle= "SmartFetch by Sohan Gogula", border_style="#F2AB46")
    console.print(panel2)

if __name__ == "__main__":
    data = {"OS": "CachyOS", "OS ID": "fedora", "OS Type": "Linux", "PC Name": "SohanLinux",
    "CPU": "Intel i9", "CPU Arch": "x86_64", "CPU%": 12.5, "CPU Count": 20, "Curr_CPU_Freq": 0.74,
    "Boost_CPU_Freq": 4.48, "RAM Used": 6.4, "RAM Total": 16.0, "RAM%": 40.0,
    "GPU": "NVIDIA RTX 3070 Ti", "VRAM Used": 0.5, "VRAM Total": 8.0,
    "Disk Used": 100.0, "Disk Total": 250.0, "Disk%": 40.0, "Boot Time": "2026-09-15 21:27:24", "Battery %": 96.74}
    text = "The PC's specifications are generally considered average..."
    render_stats(data)
    render_ai(text)
