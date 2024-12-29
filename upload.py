import subprocess
import shutil
import os

# Define paths
LOCAL_FILE = "/home/pi/NPS/data/DATA_VIS.txt"
REPO_FILE = "/home/pi/researchfarm/data.txt"
REPO_PATH = "/home/pi/researchfarm"

# Step 1: Copy the local file into the repository
shutil.copyfile(LOCAL_FILE, REPO_FILE)
print("? File copied to repository successfully.")

# Step 2: Commit and push changes to GitHub
os.chdir(REPO_PATH)

try:
    subprocess.run(["git", "add", "."], check=True)
    # Commit if there are changes, else force an empty commit
    subprocess.run(["git", "commit", "-m", "Automated update from local source"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("? Changes pushed to GitHub successfully.")
except subprocess.CalledProcessError as e:
    # Force an empty commit if no changes are detected
    if "nothing to commit, working tree clean" in str(e):
        subprocess.run(["git", "commit", "--allow-empty", "-m", "Automated update (no changes detected)"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("? Empty commit pushed successfully.")
    else:
        print(f"? Error during Git operations: {e}")
