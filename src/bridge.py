import os
import time
import pyautogui
import win32gui
import win32con
import datetime

def main():
    vibe_path = r"C:\Users\manse\HereHereHereHereroroAllCode\VibeCoding"
    cmd_path = os.path.join(vibe_path, "commands.txt")
    
    print("Bottle Auto-Bridge is running...")
    print("Keep your browser window maximized.")

    if not os.path.exists(cmd_path):
        with open(cmd_path, "w", encoding="utf-8") as f:
            f.write("# Command Queue\n")

    # Sync to current end of file
    last_count = len(open(cmd_path, "r", encoding="utf-8").readlines())

    while True:
        try:
            with open(cmd_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            if len(lines) > last_count:
                new_cmd = lines[-1].strip()
                # Skip lines that are just timestamps or empty
                if new_cmd and not new_cmd.startswith("#"):
                    print(f"Relaying command to Agent: {new_cmd}")
                    
                    # 1. Bring Browser to Foreground (Assume it's active or maximize)
                    # We'll use a safer approach: Alt+Tab or just click if maximized
                    # For safety, let's click the bottom part of the screen where chat input is.
                    screen_w, screen_h = pyautogui.size()
                    input_x, input_y = screen_w // 2, screen_h - 100
                    
                    pyautogui.click(input_x, input_y)
                    time.sleep(0.5)
                    
                    # 2. Type and Enter
                    pyautogui.typewrite(f"Bottle, roro says: {new_cmd}")
                    pyautogui.press('enter')
                    
                last_count = len(lines)
            
            time.sleep(2)
        except Exception as e:
            print(f"Bridge Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()
