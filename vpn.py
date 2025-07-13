# vpn.py

import subprocess
import time

def connect_vpn():
    try:
        subprocess.run(["windscribe", "disconnect"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        # Optional: Change to a specific location
        location = "best"  # or "US", "CA", etc.
        result = subprocess.run(["windscribe", "connect", location], capture_output=True, text=True)
        if "Connected" in result.stdout:
            print(f"[✓] VPN connected ({location})")
            return True
        else:
            print(f"[X] VPN connect failed: {result.stdout.strip()}")
            return False
    except Exception as e:
        print(f"[X] VPN error: {e}")
        return False

def disconnect_vpn():
    try:
        subprocess.run(["windscribe", "disconnect"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("[*] VPN disconnected.")
    except:
        pass