import psutil
import platform
import datetime

def get_status():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    batt = psutil.sensors_battery()
    
    print("="*30)
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem}%")
    if batt:
        status = "Charging" if batt.power_plugged else "Discharging"
        print(f"Battery: {batt.percent}% ({status})")
    else:
        print("Battery: N/A")
    print("="*30)

if __name__ == "__main__":
    get_status()
