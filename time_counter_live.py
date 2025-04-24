import time
import os
import subprocess

PROGRESS_FILE = "progress.txt"
SAVE_INTERVAL = 60  # Save and push every 60 seconds

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return int(f.read().strip())
    return 0

def save_progress(seconds):
    with open(PROGRESS_FILE, "w") as f:
        f.write(str(seconds))

def git_commit_push():
    subprocess.run(["git", "add", PROGRESS_FILE])
    subprocess.run(["git", "commit", "-m", "⏱️ Auto-update progress"])
    subprocess.run(["git", "push"])

def main():
    elapsed = load_progress()
    print(f"Resuming from {elapsed} seconds...")

    try:
        while True:
            time.sleep(1)
            elapsed += 1
            print(f"\r⏳ Elapsed: {elapsed}s", end="", flush=True)

            if elapsed % SAVE_INTERVAL == 0:
                save_progress(elapsed)
                git_commit_push()

    except KeyboardInterrupt:
        save_progress(elapsed)
        git_commit_push()
        print(f"\n⏹️ Final progress saved: {elapsed}s")

if __name__ == "__main__":
    main()
