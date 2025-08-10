import time
import random
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, delay=0.02, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task, length=20, color=Fore.GREEN):
    slow_print(f"[+] {task}", 0.02, Fore.CYAN)
    for i in range(length + 1):
        bar = "#" * i + "-" * (length - i)
        sys.stdout.write(color + f"\r[{bar}] {i*5}%" + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def fake_login():
    slow_print("[*] Connecting to server...", 0.02, Fore.YELLOW)
    time.sleep(1)
    loading_bar("User authorization", 20, Fore.MAGENTA)
    slow_print("[+] Access granted! ID: ROOT_ADMIN_1337", 0.02, Fore.GREEN)

def port_scan():
    slow_print("[*] Scanning ports...", 0.02, Fore.YELLOW)
    open_ports = random.sample(range(20, 100), 5)
    for port in range(20, 100):
        color = Fore.GREEN if port in open_ports else Fore.RED
        sys.stdout.write(f"\rPort {port} ... {color}{'open' if port in open_ports else 'closed'}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.03)
    print("\n" + Fore.CYAN + "[+] Found opened ports: " + ", ".join(map(str, open_ports)) + Style.RESET_ALL)

def file_list():
    slow_print("[*] Reading file list...", 0.02, Fore.YELLOW)
    fake_files = [
        "secret_plans.txt", "bank_accounts.csv", "passwords.enc",
        "nuclear_codes.bin", "top_secret.pdf"
    ]
    for f in fake_files:
        slow_print(f"  -> {f}", 0.02, Fore.CYAN)
        time.sleep(0.2)

def decrypt_files():
    slow_print("[*] Decrypting files...", 0.02, Fore.YELLOW)
    for i in range(1, 6):
        if random.randint(0, 5) == 3:
            slow_print(f"[!] Error when decrypting file {i}", 0.02, Fore.RED)
        else:
            slow_print(f"File {i} decrypted: OK", 0.02, Fore.GREEN)
        time.sleep(0.3)

def main():
    os.system("cls" if os.name == "nt" else "clear")
    slow_print("=== HACKER UTILITY 3000 ===", 0.05, Fore.GREEN)
    fake_login()
    port_scan()
    file_list()
    decrypt_files()
    slow_print("[+] Task completed. All data loaded to server.", 0.02, Fore.GREEN)
    slow_print("Closing connection...", 0.02, Fore.YELLOW)
    time.sleep(1)
    slow_print("[DISCONNECTED]", 0.02, Fore.RED)

if __name__ == "__main__":
    main()
