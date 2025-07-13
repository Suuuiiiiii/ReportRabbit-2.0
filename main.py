# main.py

import os
import time
from reporter import report_target_account
from account_creator import create_instagram_account
from vpn import connect_vpn, disconnect_vpn
from utils import clear_terminal, banner

TARGET_FILE = "targets.txt"  # List of usernames to report

def load_targets():
    if not os.path.exists(TARGET_FILE):
        print("[!] targets.txt not found. Create it with usernames to report.")
        return []
    with open(TARGET_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def menu():
    clear_terminal()
    banner()
    print("\n[1] Create & Report a Target")
    print("[2] Exit")
    return input("\nSelect an option: ").strip()

def main():
    while True:
        choice = menu()

        if choice == "1":
            targets = load_targets()
            if not targets:
                print("[!] No targets found in targets.txt.")
                time.sleep(2)
                continue

            for username in targets:
                print(f"\n[*] Target: @{username}")
                print("[*] Rotating VPN...")
                if not connect_vpn():
                    print("[X] VPN connection failed.")
                    continue

                print("[*] Creating Instagram account...")
                session = create_instagram_account()
                if not session:
                    print("[X] Account creation failed.")
                    continue

                print("[*] Reporting target account...")
                report_target_account(username, session)

                print("[*] Disconnecting VPN...")
                disconnect_vpn()

                time.sleep(5)  # Optional: Delay between cycles

        elif choice == "2":
            print("\n[+] Exiting ReportRabbit.")
            break

        else:
            print("[!] Invalid selection.")
            time.sleep(1)

if __name__ == "__main__":
    main()