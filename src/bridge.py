import os
import time
import pyautogui
import datetime

def main():
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    cmd_path = os.path.join(vibe_path, "commands.txt")
    
    print("Bottle Bridge System Starting...")

    if not os.path.exists(cmd_path):
        with open(cmd_path, "w", encoding="utf-8") as f: f.write("# Queue\n")

    last_count = len(open(cmd_path, "r", encoding="utf-8").readlines())

    while True:
        try:
            with open(cmd_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            if len(lines) > last_count:
                new_cmd = lines[-1].strip()
                print(f"Relaying: {new_cmd}")
                
                # Bring browser to front using simple Alt+Tab or just typing
                # We assume the browser is the active window.
                pyautogui.typewrite(new_cmd)
                pyautogui.press('enter')
                
                last_count = len(lines)
            
            time.sleep(2)
        except Exception as e:
            time.sleep(5)

if __name__ == "__main__":
    main()
