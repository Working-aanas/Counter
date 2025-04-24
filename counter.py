import time
import sys

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0 or hours > 0:
        parts.append(f"{minutes}min")
    parts.append(f"{secs}s")

    return " ".join(parts)

def countdown():
    counter = 1
    try:
        while True:
            time_str = format_time(counter)
            sys.stdout.write(f"\r{time_str}   ")
            sys.stdout.flush()
            time.sleep(1)
            counter += 1
    except KeyboardInterrupt:
        print("\nTimer stopped.")

if __name__ == "__main__":
    countdown()
