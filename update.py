import subprocess
import shutil
import os

# paths defining
LOCAL_FILE = "/media/pi/9E8E534B8E531B5B1/data/AGDaMo_Dec9.txt"
REPO_FILE = "/home/pi/researchfarm/data.txt"
REPO_PATH = "/home/pi/researchfarm"


shutil.copyfile(LOCAL_FILE, REPO_FILE)
print("? File copied to repository successfully.")

#initial commit
os.chdir(REPO_PATH)

try:
    # Existing commits
    status_output = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status_output.stdout.strip():
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Automated update from local source"], check=True)
        print("? Changes committed successfully.")
    else:
        print("?? No changes detected. Skipping commit.")

    # push changes
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("? Changes pushed to GitHub successfully.")

except subprocess.CalledProcessError as e:
    print(f"? Error during Git operations.")
    print(f"STDOUT: {e.stdout}")
    print(f"STDERR: {e.stderr}") # This is where the real secret is!
