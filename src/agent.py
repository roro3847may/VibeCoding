import os
import time
import datetime
import psutil
import sys

# Ensure UTF-8 for Korean support
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

def main():
    # Integrated vcd: Move to project root
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    os.chdir(vibe_path)
    
    cmd_path = os.path.join(vibe_path, "commands.txt")
    log_path = os.path.join(vibe_path, "agent_log.txt")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("      OPENCODE REMOTE AGENT INTERFACE")
    print("==========================================")
    print(f"Project: {os.getcwd()}")
    print(f"System:  {get_system_summary()}")
    print("-" * 42)
    print(" Commands: vstatus, vhelp, exit")
    print(" Type your request for the Agent below.")
    print("-" * 42)

    # Log monitoring logic
    last_log_pos = os.path.getsize(log_path) if os.path.exists(log_path) else 0

    while True:
        try:
            # Check for Agent's response from agent_log.txt
            if os.path.exists(log_path):
                current_size = os.path.getsize(log_path)
                if current_size > last_log_pos:
                    with open(log_path, "r", encoding="utf-8") as f:
                        f.seek(last_log_pos)
                        new_content = f.read()
                        if new_content.strip():
                            # Clear line and print Agent's response
                            print(f"\n[Agent]: {new_content.strip()}")
                        last_log_pos = current_size

            # User input
            prompt = input("\n[User]> ").strip()
            
            if not prompt: continue
            
            if prompt.lower() == 'exit':
                print("Closing session...")
                break
            elif prompt.lower() == 'vstatus':
                print(f"\n[System Status] {get_system_summary()}")
                continue
            elif prompt.lower() == 'vhelp':
                print("\n--- Commands ---")
                print("vstatus : Check laptop status")
                print("vhelp   : Show this help")
                print("exit    : Close session")
                print("Other   : Any coding request")
                continue
            
            # Save command to commands.txt
            with open(cmd_path, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"[{now}] {prompt}\n")
            
            print(f" >> Sent. Opencode is working on it...")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
