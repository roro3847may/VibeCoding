import os
import time
import datetime
import psutil
import sys
import threading

# Ensure UTF-8 encoding for Korean support in Windows terminal
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

def get_system_summary():
    try:
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        batt = psutil.sensors_battery()
        status = "Charging" if batt and batt.power_plugged else "Discharging"
        batt_pct = f"{batt.percent}% ({status})" if batt else "N/A"
        return f"CPU: {cpu}% | RAM: {mem}% | Battery: {batt_pct}"
    except:
        return "Status N/A"

def monitor_logs(log_path, stop_event):
    """Monitors agent_log.txt and prints new content immediately."""
    if not os.path.exists(log_path):
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("--- Log Initialized ---\n")
            
    last_log_pos = os.path.getsize(log_path)
    
    while not stop_event.is_set():
        if os.path.exists(log_path):
            current_size = os.path.getsize(log_path)
            if current_size > last_log_pos:
                with open(log_path, "r", encoding="utf-8") as f:
                    f.seek(last_log_pos)
                    new_content = f.read()
                    if new_content.strip():
                        sys.stdout.write(f"\n[Bottle]: {new_content.strip()}\n[User]> ")
                        sys.stdout.flush()
                    last_log_pos = current_size
        time.sleep(0.5)

def main():
    # Force project directory
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    os.chdir(vibe_path)
    
    # Improved Monitor Power Off command
    try:
        os.system("powershell -Command \"Add-Type -TypeDefinition '[DllImport(\\\"user32.dll\\\")] public static extern int PostMessage(int hWnd, int hMsg, int wParam, int lParam);'; [Win32Functions.Win32PostMessage]::PostMessage(0xffff, 0x0112, 0xf170, 2)\" > nul 2>&1")
    except:
        pass
    
    cmd_path = os.path.join(vibe_path, "commands.txt")
    log_path = os.path.join(vibe_path, "agent_log.txt")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("  ____   ____ _______ _______ _      ______ ")
    print(" |  _ \\ / __ \\__   __|__   __| |    |  ____|")
    print(" | |_) | |  | | | |     | |  | |    | |__   ")
    print(" |  _ <| |  | | | |     | |  | |    |  __|  ")
    print(" | |_) | |__| | | |     | |  | |____| |____ ")
    print(" |____/ \\____/  |_|     |_|  |______|______|")
    print(" ==========================================")
    print(f" System: {get_system_summary()}")
    print(" Commands: vstatus, vhelp, exit")
    print("-" * 42)

    stop_event = threading.Event()
    log_thread = threading.Thread(target=monitor_logs, args=(log_path, stop_event), daemon=True)
    log_thread.start()

    try:
        while True:
            prompt = input("[User]> ").strip()
            
            if not prompt: continue
            
            if prompt.lower() == 'exit':
                stop_event.set()
                break
            elif prompt.lower() == 'vstatus':
                print(f"[System Status] {get_system_summary()}")
                continue
            elif prompt.lower() == 'vhelp':
                print("\n--- Available Commands ---")
                print("vstatus : Current laptop hardware status")
                print("vhelp   : Show this manual")
                print("exit    : Close this session")
                print("--------------------------")
                continue
            
            with open(cmd_path, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"[{now}] {prompt}\n")
            
            print(f" >> Request logged. Bottle is processing...")

    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        print("\nSession ended.")

if __name__ == "__main__":
    main()
