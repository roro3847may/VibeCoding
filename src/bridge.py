import os
import time
import datetime

def main():
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    cmd_path = os.path.join(vibe_path, "commands.txt")
    log_path = os.path.join(vibe_path, "agent_log.txt")
    
    if not os.path.exists(cmd_path):
        with open(cmd_path, "w", encoding="utf-8") as f:
            f.write("# Start\n")
            
    last_count = len(open(cmd_path, "r", encoding="utf-8").readlines())
    
    while True:
        try:
            with open(cmd_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            if len(lines) > last_count:
                new_cmd = lines[-1].strip()
                # Simplified acknowledgment as requested by roro
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write("\n[Bottle]: k\n")
                
                print(f"NEW_COMMAND: {new_cmd}")
                last_count = len(lines)
            
            time.sleep(1)
        except:
            time.sleep(5)

if __name__ == "__main__":
    main()
