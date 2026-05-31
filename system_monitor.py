import psutil
import socket
import time
import os

def get_cpu_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    return temp.replace("temp=", "").strip()

while True:
    os.system('clear')

    cpu_usage = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    uptime = time.time() - psutil.boot_time()

    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("========================")
    print(" CYBERDECK SYSTEM STATUS ")
    print("========================\n")

    print(f"CPU Usage:      {cpu_usage}%")
    print(f"RAM Usage:      {ram.percent}%")
    print(f"CPU Temp:       {get_cpu_temp()}")
    print(f"Disk Usage:     {disk.percent}%")
    print(f"System Uptime:  {hours}h {minutes}m")
    print(f"IP Address:     {ip_address}")

    print("\nSTATUS: STABLE")

    time.sleep(2)
