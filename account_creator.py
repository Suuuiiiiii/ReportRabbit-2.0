# account_creator.py

import random
import string
import time
from playwright.sync_api import sync_playwright
from mailtm import MailTMClient
from captcha_solver import solve_recaptcha

def random_username():
    return "user" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

def random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^", k=12))

def create_instagram_account():
    email_client = MailTMClient()
    email, token = email_client.generate_address()
    print(f"[*] Generated temp email: {email}")

    name = "John Doe"
    username = random_username()
    password = random_password()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Visit signup page
            page.goto("https://www.instagram.com/accounts/emailsignup/", timeout=60000)
            page.wait_for_selector("input[name=emailOrPhone]", timeout=20000)

            # Fill out the form
            print("[*] Filling out signup form...")
            page.fill("input[name=emailOrPhone]", email)
            page.fill("input[name=fullName]", name)
            page.fill("input[name=username]", username)
            page.fill("input[name=password]", password)
            page.click("button[type=submit]")

            # Wait for birthday page
            page.wait_for_selector("select[title='Year']", timeout=15000)

            # Birthday selection (Year: 2000, Month/Day: random valid)
            print("[*] Selecting birthday...")
            page.select_option("select[title='Year']", "2000")
            page.select_option("select[title='Month']", str(random.randint(1, 12)))
            page.select_option("select[title='Day']", str(random.randint(1, 28)))
            page.click("button[type=submit]")

            # Wait for reCAPTCHA
            print("[*] Solving CAPTCHA...")
            sitekey = "6LdktRgnAAAAAFQ6icovYI2-masYLFjEFyzQzpix"
            page_url = "https://www.instagram.com/accounts/emailsignup/"
            token = solve_recaptcha(sitekey, page_url)

            page.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML = "{token}";')
            page.evaluate('''() => {
                document.querySelector('form').submit();
            }''')

            # Wait for email verification
            print("[*] Waiting for verification code...")
            code = email_client.wait_for_code(timeout=120)
            if not code:
                print("[X] No code received.")
                return None

            page.wait_for_selector("input[name=email_confirmation_code]", timeout=20000)
            page.fill("input[name=email_confirmation_code]", code)
            page.click("button[type=submit]")

            print(f"[✓] Account created: @{username}")
            return page  # Return active session

        except Exception as e:
            print(f"[X] Signup failed: {e}")
            return None

        finally:
            # Keep browser open for inspection, or close it if not needed
            pass