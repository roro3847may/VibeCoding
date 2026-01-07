import os
import time
import datetime
import psutil
import platform

def get_system_summary():
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    batt = psutil.sensors_battery()
    status = "Charging" if batt and batt.power_plugged else "Discharging"
    batt_pct = f"{batt.percent}% ({status})" if batt else "N/A"
    return f"CPU: {cpu}% | RAM: {mem}% | Battery: {batt_pct}"

def print_help():
    print("\n--- Available Commands ---")
    print("vstatus : Show detailed system status")
    print("vhelp   : Show this help")
    print("exit    : Close the session")
    print("Other   : Send message to Opencode Agent")
    print("--------------------------")

def main():
    cmd_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding\commands.txt"
    log_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding\agent_log.txt"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("      🤖 OPENCODE INTEGRATED CONSOLE")
    print("==========================================")
    print(f"Status: {get_system_summary()}")
    print("Type your request or 'vhelp' for info.")
    print("-" * 42)

    last_log_pos = os.path.getsize(log_path) if os.path.exists(log_path) else 0

    while True:
        try:
            # 1. 실시간 로그 체크 (Agent의 답변 출력)
            if os.path.exists(log_path):
                current_size = os.path.getsize(log_path)
                if current_size > last_log_pos:
                    with open(log_path, "r", encoding="utf-8") as f:
                        f.seek(last_log_pos)
                        new_logs = f.read().strip()
                        if new_logs:
                            print(f"\n[Agent]: {new_logs}")
                        last_log_pos = current_size

            # 2. 사용자 입력
            prompt = input("\nRequest > ").strip()
            
            if not prompt: continue
            
            if prompt.lower() in ['exit', 'quit', '종료']:
                print("Goodbye!")
                break
            
            # 3. 내부 명령어 처리
            if prompt.lower() == 'vstatus':
                print(f"\n[System Status]\n{get_system_summary()}")
                continue
            elif prompt.lower() == 'vhelp':
                print_help()
                continue
            
            # 4. 에이전트에게 명령 전달
            with open(cmd_path, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%H:%M:%S")
                f.write(f"[{now}] {prompt}\n")
            
            print(f" >> Request logged at {now}. Waiting for Opencode...")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
