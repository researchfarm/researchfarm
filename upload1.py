import subprocess
import shutil
import os
from datetime import datetime

LOCAL_FILE = "/media/pi/9E8E534B8E531B5B1/data/AGDaMo_Dec9.txt"
REPO_FILE = "/home/pi/researchfarm/data.txt"
REPO_PATH = "/home/pi/researchfarm"

def sync():
    # 1. Copy file
    if os.path.exists(LOCAL_FILE):
        shutil.copyfile(LOCAL_FILE, REPO_FILE)
        print("? File copied locally.")
    else:
        print("? Source file missing!")
        return

    os.chdir(REPO_PATH)

    try:
        # 2. Force add the specific file (don't rely on status)
        subprocess.run(["git", "add", "data.txt"], check=True)
        
        # 3. Commit (The '|| true' allows the script to continue even if nothing changed)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        subprocess.run(["git", "commit", "-m", f"Data Update: {timestamp}"], check=False)
        
        # 4. Push
        result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
        
        if "Everything up-to-date" in result.stdout:
            print("?? GitHub already has this version.")
        else:
            print(f"?? Pushed to GitHub at {timestamp}")

    except Exception as e:
        print(f"? Error: {e}")

if __name__ == "__main__":
    sync()
