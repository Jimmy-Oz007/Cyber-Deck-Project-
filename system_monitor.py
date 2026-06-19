import os
import time
import psutil
import socket

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "No Network"

def get_cpu_temp():
    try:
        temp = os.popen("vcgencmd measure_temp").readline()
        return temp.replace("temp=", "").strip()
    except:
        return "Unavailable"

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    hours = int(uptime_seconds // 3600)
    minutes = int((uptime_seconds % 3600) // 60)
    return f"{hours}h {minutes}m"

while True:
    os.system("clear")

    print("=" * 40)
    print("      CYBERDECK DASHBOARD V2")
    print("=" * 40)

    print(f"CPU Usage:     {psutil.cpu_percent()}%")
    print(f"CPU Temp:      {get_cpu_temp()}")
    print(f"RAM Usage:     {psutil.virtual_memory().percent}%")
    print(f"Disk Usage:    {psutil.disk_usage('/').percent}%")
    print(f"IP Address:    {get_ip()}")
    print(f"Uptime:        {get_uptime()}")

    print()
    print(time.strftime("%Y-%m-%d"))
    print(time.strftime("%H:%M:%S"))

    print()
    print("STATUS: ONLINE")
    print("=" * 40)

    time.sleep(1)
