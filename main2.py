import os
import time
import random
import string

GREEN = "\033[92m"
RESET = "\033[0m"


def print_green(text, end='\n'):
    print(f"{GREEN}{text}{RESET}", end=end)


def clear():

    os.system('cls' if os.name == 'nt' else 'clear')


def fake_ip():
    return '.'.join(str(random.randint(1, 254)) for _ in range(4))


def generate_base64_like(size):
    chars = string.ascii_letters + string.digits + "+/="
    return ''.join(random.choice(chars) for _ in range(size))


def generate_progress_steps():
    steps = []
    current = 10
    while current < 100:
        current += random.randint(5, 25)
        if current >= 100:
            current = 100
        steps.append(current)
    return steps


def print_progress_bar_random(message):
    total = 30
    percentages = generate_progress_steps()
    for percent in percentages:
        filled_length = int(total * (percent / 100))
        bar = '█' * filled_length + '-' * (total - filled_length)
        print_green(f"{message} [{bar}] {percent}%")
        time.sleep(0.2)
    print_green(f"{message} [{'█' * total}] 100%...DONE\n")


def save_hacker_file(filename, size_kb):
    size_bytes = size_kb * 1024
    content = generate_base64_like(size_bytes)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    clear()
    print_green("Connecting to secure shell @root@darkweb.node...")
    time.sleep(1)

    print_green("Authorizing as admin@target.net...")
    time.sleep(1)
    token = ''.join(random.choice('abcdef0123456789') for _ in range(40))
    print_green(f"Access Granted. Session token: {token}\n")
    time.sleep(0.5)

    print_green("[*] Pinging dark nodes...")
    for _ in range(3):
        ip = fake_ip()
        delay = random.randint(10, 120)
        print_green(f"Pinging {ip}... Reply from {ip}: time={delay}ms")
        time.sleep(0.3)
    print()

    print_green("[*] Scanning open ports...")
    for port in range(22, 29):
        status = random.choice(["OPEN", "FILTERED"])
        print_green(f"Port {port}: {status}")
        time.sleep(0.2)
    print()

    print_green("[!] Intrusion Detection System triggered!")
    print_progress_bar_random("[*] Disabling IDS")
    print_progress_bar_random("[*] Bypassing firewall")
    print_progress_bar_random("[*] Escalating privileges")
    print_progress_bar_random("[*] Decrypting internal data")

    print_green("[*] System logs:")
    for _ in range(6):
        timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
        msg = random.choice([
            "Root shell initialized.",
            "System time overridden.",
            "Packet forwarding enabled.",
            "Logs wiped successfully.",
            "Remote host unlocked.",
            "SSH keys extracted."
        ])
        print_green(f"{timestamp} {msg}")
        time.sleep(0.4)
    print()

    print_green("[*] Downloading sensitive files...")
    for _ in range(3):
        filename = f"sensfile_dump_{random.randint(1000, 9999)}.dat"
        size_kb = random.randint(5, 15)
        print_green(f"    Downloaded {filename} ({size_kb} KB)")
        save_hacker_file(filename, size_kb)
        time.sleep(0.3)

    print_green("\n[✓] All operations complete.")


if __name__ == "__main__":
    main()
