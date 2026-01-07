import os
import time
import sys
import threading
import psutil

if sys.platform == "win32":
    os.system("chcp 65001 > nul")

def get_sys():
    try:
        b = psutil.sensors_battery()
        p = f"{b.percent}%" if b else "N/A"
        s = "Charging" if b and b.power_plugged else "Discharging"
        return f"CPU: {psutil.cpu_percent()}% | Battery: {p} ({s})"
    except: return "Status N/A"

def monitor_agent_voice(log_path, stop_event):
    """Prints newly added lines from agent_log.txt instantly."""
    if not os.path.exists(log_path):
        with open(log_path, "w", encoding="utf-8") as f: f.write("--- Session Started ---\n")
    
    last_pos = os.path.getsize(log_path)
    
    while not stop_event.is_set():
        if os.path.exists(log_path):
            curr_size = os.path.getsize(log_path)
            if curr_size > last_pos:
                with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
                    f.seek(last_pos)
                    text = f.read().strip()
                    if text:
                        # Clear existing line and print Bottle's message
                        sys.stdout.write(f"\r{text}\n[User]> ")
                        sys.stdout.flush()
                    last_pos = curr_size
        time.sleep(0.5)

def main():
    path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    os.chdir(path)
    
    cmd_f = "commands.txt"
    log_f = "agent_log.txt"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("      BOTTLE AUTO-BRIDGE INTERFACE")
    print("==========================================")
    print(f" {get_sys()}")
    print(" Commands: vstatus, vhelp, exit")
    print("-" * 42)

    stop_event = threading.Event()
    threading.Thread(target=monitor_agent_voice, args=(log_f, stop_event), daemon=True).start()

    try:
        while True:
            p = input("[User]> ").strip()
            if not p: continue
            if p.lower() == 'exit': break
            if p.lower() == 'vstatus':
                print(f"\n[Status] {get_sys()}")
                continue
            
            # Write to commands.txt to trigger bridge.py
            with open(cmd_f, "a", encoding="utf-8") as f:
                f.write(f"{p}\n")
            
            print(f" >> Sent to Bridge. Waking up Bottle...")

    except KeyboardInterrupt: pass
    finally: stop_event.set()

if __name__ == "__main__":
    main()
