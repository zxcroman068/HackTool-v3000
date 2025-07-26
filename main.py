import time
import random
import os
import string

GREEN = "\033[92m"
RESET = "\033[0m"


def generate_hacker_data(size):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:,.<>/?\\|"
    return ''.join(random.choice(chars) for _ in range(size))


def save_hacker_file(filename, size_kb):
    size_bytes = size_kb * 1024
    content = generate_hacker_data(size_bytes)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def fake_ip():
    return '.'.join(str(random.randint(1, 254)) for _ in range(4))


def print_green(text, end='\n'):
    print(f"{GREEN}{text}{RESET}", end=end)


def print_progress_bar_random(message):
    total = 30
    percentages = []
    current = 0
    while current < 100:
        step = random.randint(5, 20)
        current = min(current + step, 100)
        percentages.append(current)

    for percent in percentages:
        filled_length = int(total * (percent / 100))
        bar = '█' * filled_length + '-' * (total - filled_length)
        print_green(f"{message} [{bar}] {percent}%")
        time.sleep(0.3)

    print_green(f"{message} [{'█' * total}] 100%...DONE\n")


def generate_progress_steps(count=5, max_value=95):
    steps = []
    current = 10
    for _ in range(count):
        increment = random.randint(5, 30)
        current += increment
        if current >= max_value:
            break
        steps.append(min(current, max_value))
    steps.append(100)
    return steps


def main():
    print_green("Initializing system...")
    time.sleep(1)

    for _ in range(20):
        src = fake_ip()
        dst = fake_ip()
        data_size = random.randint(100, 10000)
        print_green(f"[INFO] Sending {data_size} bytes from {src} to {dst}...")
        time.sleep(0.2)

    print()
    print_progress_bar_random("[*] Establishing secure connection to darkweb node")
    time.sleep(0.5)
    print_progress_bar_random("[*] Bypassing firewall")
    print_progress_bar_random("[*] Injecting payload")
    print_progress_bar_random("[*] Encrypting data stream")

    print()
    progress_values = generate_progress_steps()
    for percent in progress_values:
        print_green(f"[+] Hack in progress... {percent}% complete")
        time.sleep(0.4)

    print()
    print_green("[!] ACCESS GRANTED")
    print_green("[*] Downloading files...")
    for _ in range(3):
        filename = f"secret_file_{random.randint(100, 999)}.dat"
        size_kb = random.randint(1, 10)
        print_green(f"    Downloaded {filename} ({size_kb} MB)")
        save_hacker_file(filename, size_kb)
        time.sleep(0.3)

    print()
    print_green("[✓] Mission complete. System shutting down...")
    time.sleep(2)


if __name__ == "__main__":
    main()
