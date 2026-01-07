import os
import time
import datetime
import psutil
import sys

# Ensure terminal uses UTF-8 for Korean support
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
        return "System status unavailable"

def main():
    # Force move to project directory (Internal vcd)
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    os.chdir(vibe_path)
    
    cmd_path = os.path.join(vibe_path, "commands.txt")
    log_path = os.path.join(vibe_path, "agent_log.txt")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("      🤖 OPENCODE MOBILE REMOTE AGENT")
    print("==========================================")
    print(f"Current Path: {os.getcwd()}")
    print(f"Status: {get_system_summary()}")
    print("-" * 42)
    print("Commands: vstatus, vhelp, exit")
    print("Or type anything to talk to Opencode Agent.")
    print("-" * 42)

    # Initialize log pointer to end of file to see only new messages
    last_log_pos = os.path.getsize(log_path) if os.path.exists(log_path) else 0

    while True:
        try:
            # 1. Real-time Log Monitoring (Agent -> Mobile)
            if os.path.exists(log_path):
                current_size = os.path.getsize(log_path)
                if current_size > last_log_pos:
                    with open(log_path, "r", encoding="utf-8") as f:
                        f.seek(last_log_pos)
                        new_content = f.read()
                        if new_content.strip():
                            print(f"\n{new_content.strip()}")
                        last_log_pos = current_size

            # 2. Non-blocking input or short sleep to keep UI responsive
            # Note: Standard input() is blocking, but we check logs after each input.
            prompt = input("\n[Mobile Request]> ").strip()
            
            if not prompt: continue
            
            if prompt.lower() == 'exit':
                print("Closing Remote Agent Session...")
                break
            elif prompt.lower() == 'vstatus':
                print(f"\n[System Status] {get_system_summary()}")
                continue
            elif prompt.lower() == 'vhelp':
                print("\n--- Commands ---")
                print("vstatus : System info")
                print("vhelp   : Show this")
                print("exit    : Quit")
                print("Others  : Agent command")
                continue
            
            # 3. Log user command for Agent to see
            with open(cmd_path, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"[{now}] {prompt}\n")
            
            print(f" >> Sent to Agent. Watching for response...")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
