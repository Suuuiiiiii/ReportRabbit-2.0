# captcha_solver.py

import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CAPTCHA_API_KEY")
BASE_URL = "http://2captcha.com"

def solve_recaptcha(sitekey: str, page_url: str) -> str:
    print("[*] Sending CAPTCHA to 2Captcha...")

    payload = {
        "key": API_KEY,
        "method": "userrecaptcha",
        "googlekey": sitekey,
        "pageurl": page_url,
        "json": 1
    }

    try:
        # Step 1: Submit CAPTCHA
        r = requests.post(f"{BASE_URL}/in.php", data=payload)
        rid = r.json().get("request")
        if r.json().get("status") != 1:
            raise Exception(f"2Captcha error: {r.json().get('request')}")

        print(f"[*] CAPTCHA ID: {rid} — waiting for solution...")

        # Step 2: Poll for result
        for _ in range(20):  # ~40–60s max
            time.sleep(5)
            res = requests.get(f"{BASE_URL}/res.php?key={API_KEY}&action=get&id={rid}&json=1")
            if res.json().get("status") == 1:
                print("[✓] CAPTCHA solved.")
                return res.json().get("request")
            elif res.json().get("request") == "CAPCHA_NOT_READY":
                continue
            else:
                raise Exception(f"2Captcha failed: {res.json().get('request')}")

        raise TimeoutError("[X] CAPTCHA solving timed out.")

    except Exception as e:
        print(f"[X] CAPTCHA solve failed: {e}")
        return ""