import os
import time
import datetime

def main():
    cmd_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding\commands.txt"
    log_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding\agent_log.txt"
    
    # Ensure files exist
    if not os.path.exists(log_path):
        with open(log_path, "w", encoding="utf-8") as f:
            f.write("=== Agent Log Started ===\n")

    os.system('cls' if os.name == 'nt' else 'clear')
    print("==========================================")
    print("      🤖 OPENCODE REAL-TIME CONSOLE")
    print("==========================================")
    print(" * Type your request to the Agent.")
    print(" * Type 'exit' to quit.")
    print("-" * 42)

    last_log_pos = os.path.getsize(log_path)

    while True:
        try:
            # Check for new logs from Agent
            current_size = os.path.getsize(log_path)
            if current_size > last_log_pos:
                with open(log_path, "r", encoding="utf-8") as f:
                    f.seek(last_log_pos)
                    new_logs = f.read()
                    if new_logs.strip():
                        print(f"\n[Agent]: {new_logs.strip()}")
                    last_log_pos = current_size

            # Get user input
            user_input = input("\nRequest > ")
            if user_input.lower() in ['exit', 'quit']:
                break
            
            if not user_input.strip():
                continue
            
            # Send command
            with open(cmd_path, "a", encoding="utf-8") as f:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{now}] {user_input}\n")
            
            print(" >> Sending request... [OK]")
            print(" >> Waiting for Agent response...", end="", flush=True)
            
            # Simple progress animation
            for _ in range(5):
                print(".", end="", flush=True)
                time.sleep(0.3)
            print(" [Logged]")

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
