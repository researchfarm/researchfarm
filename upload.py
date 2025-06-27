import subprocess
import shutil
import os

# Define paths
LOCAL_FILE = "/media/pi/9E8E534B8E531B5B1/data/Test_Usha121.txt"
REPO_FILE = "/home/pi/researchfarm/data.txt"
REPO_PATH = "/home/pi/researchfarm"

# Step 1: Copy the local file into the repository
shutil.copyfile(LOCAL_FILE, REPO_FILE)
print("? File copied to repository successfully.")

# Step 2: Commit and push changes to GitHub
os.chdir(REPO_PATH)

try:
    # Check if there are changes to commit
    status_output = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if status_output.stdout.strip():
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Automated update from local source"], check=True)
        print("? Changes committed successfully.")
    else:
        print("?? No changes detected. Skipping commit.")

    # Ensure SSH is used and push changes
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("? Changes pushed to GitHub successfully.")

except subprocess.CalledProcessError as e:
    print(f"? Error during Git operations: {e}")
