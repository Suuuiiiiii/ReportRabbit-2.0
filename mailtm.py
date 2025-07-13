# mailtm.py

import requests
import time
import random
import string

class MailTMClient:
    def __init__(self):
        self.base = "https://api.mail.tm"
        self.session = requests.Session()
        self.token = None
        self.address = None
        self.password = self._random_password()

    def _random_password(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=12))

    def generate_address(self):
        domain = self.session.get(f"{self.base}/domains").json()["hydra:member"][0]["domain"]
        self.address = f"{self._random_username()}@{domain}"

        payload = {
            "address": self.address,
            "password": self.password
        }

        # Register new email
        r = self.session.post(f"{self.base}/accounts", json=payload)
        if r.status_code != 201 and "already exists" not in r.text:
            raise Exception(f"[X] Mail.tm account creation failed: {r.text}")

        # Login to get token
        auth = {
            "address": self.address,
            "password": self.password
        }
        res = self.session.post(f"{self.base}/token", json=auth)
        self.token = res.json()["token"]
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

        return self.address, self.token

    def _random_username(self):
        return "ig" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

    def wait_for_code(self, timeout=120):
        print("[*] Waiting for Instagram code...")

        for _ in range(timeout // 5):
            time.sleep(5)
            msgs = self.session.get(f"{self.base}/messages").json()["hydra:member"]
            if not msgs:
                continue

            for msg in msgs:
                if "Instagram" in msg["from"]["address"] and "is your Instagram code" in msg["subject"]:
                    msg_data = self.session.get(f"{self.base}/messages/{msg['id']}").json()
                    return self._extract_code(msg_data["text"])

        print("[X] Timeout: No verification email received.")
        return None

    def _extract_code(self, text):
        import re
        match = re.search(r"\b(\d{6})\b", text)
        return match.group(1) if match else None