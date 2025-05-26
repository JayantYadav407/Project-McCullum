import time
import random

def simulate_rm_rf():
    # Header
    print("🌌 Initiating sudo rm -rf /* --no-preserve-root simulation 🌌\n")
    time.sleep(2)
    print("⚠️ Warning: This will 'delete' everything in a safe and sentimental simulation.")
    time.sleep(2)
    print("✨ Proceeding... in memory of your beloved grandmother. ✨\n")
    time.sleep(3)
    
    # File paths to simulate
    fake_files = [
        "/usr/local/bin/python3", "/home/user/documents/thesis.docx", 
        "/home/grandma/recipes/apple_pie.txt", "/etc/hosts", 
        "/home/user/photos/grandma_and_me.jpg", "/home/user/music/classical.mp3", 
        "/var/log/syslog", "/opt/childhood_memories.txt", 
        "/dev/null", "/usr/share/icons/smile.png", "/home/grandma/letters/love_note.txt"
    ]
    
    # Progress bar visualization
    def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
        percent = f"{100 * (iteration / float(total)):.{decimals}f}"
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="\r")
        if iteration == total:
            print()

    # Simulated deletion process
    total_files = 200
    progress_bar(0, total_files, prefix="Progress", suffix="Complete", length=40)
    for i in range(1, total_files + 1):
        file = random.choice(fake_files)
        print(f"Deleting: {file}")
        time.sleep(0.5)  # Adjust time for a minimum 2-minute runtime
        progress_bar(i, total_files, prefix="Progress", suffix="Complete", length=40)
    
    # Completion message
    print("\n💻 All files have been 'deleted'.")
    print("🌹 In memory of your grandmother, whose presence lives on in your heart.")
    print("✨ May her love continue to inspire you forever. ✨\n")

simulate_rm_rf()
