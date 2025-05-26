import time
import random

def simulate_rm_rf():
    print("Executing: sudo rm -rf /* --no-preserve-root")
    time.sleep(1)
    print("Warning: This will destroy EVERYTHING on your computer!")
    time.sleep(1)
    print("Proceeding anyway because nostalgia. ❤️")
    time.sleep(2)

    fake_files = [
        "/bin/bash", "/usr/local/bin/python3", "/home/user/documents/thesis.docx",
        "/etc/passwd", "/var/log/syslog", "/opt/funny_cat_video.mp4",
        "/dev/null", "/sys/kernel/debug", "/proc/self/mem"
    ]
    
    random.shuffle(fake_files)
    
    for i in range(1, 1010):
        file = random.choice(fake_files)
        print(f"Deleting: {file}")
        time.sleep(0.1)

    print("\n💻 Your system has been completely 'destroyed' (not really!).")
    print("🌹 In memory of your grandmother. May she rest in peace. ❤️")

simulate_rm_rf()
