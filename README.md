# 🐇 ReportRabbit (R.R)
## Porn.Down.Operation — Precision Instagram Reporting Toolkit

---

**ReportRabbit** is a fully-automated Instagram reporting framework designed for targeted takedowns of profiles violating Instagram's content policies.  
Its primary focus is on **mass-reporting accounts for "Nudity or sexual activity"**, operating with **full anonymity**, **account freshness**, and **IP rotation**.

Developed with ethical automation and clean execution in mind, it ensures **one-click activation** for every stage:  
Account creation → CAPTCHA bypass → Email verification → Target search → Report submission.

---

## 💡 Why ReportRabbit?

Instagram is flooded with adult spam accounts, porn bots, and explicit content.  
**Manual reporting is slow, limited, and ineffective at scale.**  
R.R offers a smarter way:

✅ *Fresh accounts per report*  
✅ *VPN rotation with each cycle*  
✅ *Bypasses reCAPTCHA like a ghost*  
✅ *Auto-verifies email with real-time inbox polling*  
✅ *Precision reporting — always “Nudity or sexual activity”*

---

## 🧠 Architecture Overview

main.py ├── vpn.py                → IP rotation via Windscribe ├── account_creator.py    → Full IG signup w/ Mail.tm & CAPTCHA │   ├── captcha_solver.py → 2Captcha API (reCAPTCHA v2) │   └── mailtm.py         → Temp email & inbox polling ├── reporter.py           → Target lookup & reporting └── utils.py              → Banner, terminal clear

Each module is precision-optimized.  
No bloat. No bugginess. No unnecessary threads.

---

## 📦 Features

- 🔐 **Anonymous by Design**  
  Never reuse IPs or emails. Accounts are generated, verified, and discarded instantly.

- 🛡 **VPN Integration**  
  Built-in Windscribe CLI support ensures every request comes from a different IP.

- 🤖 **reCAPTCHA Bypass (v2)**  
  Integrates seamlessly with 2Captcha for hands-free account creation.

- 📨 **Email Verification**  
  Hooks into [Mail.tm](https://mail.tm) to poll inbox and extract 6-digit codes reliably.

- 📲 **Interactive CLI Interface**  
  Command-line control with a custom banner:  
  **"R.R"** + **"Porn.Down.Operation"** — laser focused.

- 📁 **Modular**  
  Every function is isolated. Swap out Mail.tm or CAPTCHA solvers easily.

---

## ⚙️ Setup Guide

### Requirements

- Python 3.8+
- Windscribe CLI (Linux/Windows)
- A 2Captcha API key
- Git, bash, and pip3

---

### Installation

```bash
git clone https://github.com/youruser/ReportRabbit.git
cd ReportRabbit

chmod +x setup.sh
./setup.sh

This script:

Installs Python dependencies

Installs Playwright and its browsers

Creates a .env template if one doesn't exist

Checks Windscribe CLI availability



---

🧬 Configuration

Open .env and configure:

CAPTCHA_API_KEY=your_2captcha_api_key
VPN_LOCATION=best
HEADLESS=false

Key	Purpose

CAPTCHA_API_KEY	Your 2Captcha key for bypassing reCAPTCHA
VPN_LOCATION	Where to connect (e.g. best, US, NL)
HEADLESS	false = visible browser, true = silent



---

🗂 Preparing Targets

Create a file called targets.txt with one Instagram username per line:

badpornpage123
another_spam_bot
nsfw.page88


---

🚀 Launching ReportRabbit

python3 main.py

Choose:

[1] Create & Report a Target
→ The system will:

1. Connect to VPN


2. Create and verify an IG account


3. Find the target username


4. Submit a report for “Nudity or sexual activity”


5. Disconnect and move to the next



[2] Exit
→ Clean exit with terminal clear


---

🔐 Logging and Output

Currently, ReportRabbit logs all status messages to the terminal.
If needed, future versions can include:

JSON log export

Success/fail report per user

report.log file for audit trail


Let me know if you want this feature added.


---

🧰 Advanced Options (Planned)

[ ] Proxy rotation fallback if VPN fails

[ ] GUI dashboard

[ ] Threaded multi-account support

[ ] Multiple report reasons (if you decide to enable it)

[ ] Retry queue and failure caching

[ ] Telegram bot interface for remote control



---

📬 Support

For bugs, issues, or requests:

📧 Email: report0rabbit@gmail.com

I respond to:

Bug reports

Feature requests

Legitimate questions about ethical usage



---

⚠️ Legal Disclaimer

This tool is intended for educational, ethical, and moderation-support use only.

You may not use this tool to:

Harass, stalk, or target innocent individuals

Violate Instagram’s TOS for malicious gain

Automate spam, hate, or impersonation reports


> YOU are responsible for how you use ReportRabbit.
The author takes no liability for any misuse.




---

🌀 Final Words

ReportRabbit is for one purpose and one purpose only:
Targeted takedown of explicit accounts that violate platform guidelines — using automation as a force for cleanup.

No games.

No noise.

Just pure, silent execution.


R.R is online. Porn.Down.Operation is active.