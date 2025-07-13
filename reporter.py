# reporter.py

import time
from playwright.sync_api import Page

def report_target_account(username: str, session: Page):
    try:
        # Go to Instagram home
        session.goto("https://www.instagram.com/", timeout=60000)
        session.wait_for_selector("input[placeholder='Search']", timeout=15000)

        # Search for the target
        print(f"[*] Searching for @{username}...")
        search_input = session.locator("input[placeholder='Search']")
        search_input.fill(username)
        time.sleep(2)  # Let suggestions load

        # Click correct user from dropdown
        dropdown = session.locator(f"//div[text()='{username}']")
        if not dropdown or dropdown.count() == 0:
            print("[!] Account Not Found (A.N.F.)")
            return

        dropdown.first.click()
        session.wait_for_selector("header", timeout=15000)

        # Open 3-dot menu
        print("[*] Opening report menu...")
        menu_button = session.locator("svg[aria-label='Options']")  # ⋯ menu
        menu_button.click()
        session.wait_for_selector("text=Report", timeout=10000)
        session.locator("text=Report").click()

        # Start report process
        session.wait_for_selector("text=Report Account", timeout=10000)
        session.locator("text=Report Account").click()

        session.wait_for_selector("text=It's posting content that shouldn't be on Instagram", timeout=10000)
        session.locator("text=It's posting content that shouldn't be on Instagram").click()

        session.wait_for_selector("text=Nudity or sexual activity", timeout=10000)
        session.locator("text=Nudity or sexual activity").click()

        print("[✓] Report submitted successfully.")

    except Exception as e:
        print(f"[X] Reporting failed: {e}")