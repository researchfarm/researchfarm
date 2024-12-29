import subprocess
import shutil
import os

# Define paths
LOCAL_FILE = "/home/pi/NPS/data/DATA_VIS.txt"  # Local source file path
REPO_FILE = "/home/pi/researchfarm/data.txt"  # Destination in repo
REPO_PATH = "/home/pi/researchfarm"  # Local repo folder path

# Step 1: Copy the local file into the repository
shutil.copyfile(LOCAL_FILE, REPO_FILE)
print("? File copied to repository successfully.")

# Step 2: Commit and push changes to GitHub
os.chdir(REPO_PATH)

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Automated update from local source"], check=True)
    subprocess.run(["git", "push"], check=True)
    print("? Changes pushed to GitHub successfully.")
except subprocess.CalledProcessError as e:
    print(f"? Error during Git operations: {e}")
