#!/bin/bash

echo ">> ReportRabbit Setup Starting..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[X] Python3 not found. Please install Python 3.8+."
    exit 1
fi

# Install dependencies
echo ">> Installing Python dependencies..."
pip3 install -r requirements.txt

# Install Playwright browsers
echo ">> Installing Playwright browsers..."
playwright install

# Check Windscribe
if ! command -v windscribe &> /dev/null; then
    echo "[!] Windscribe CLI not found. You must install and login manually."
else
    echo "[✓] Windscribe CLI found."
fi

# Confirm .env is set
if [ ! -f ".env" ]; then
    echo "[!] .env file not found. Creating template..."
    cat <<EOF > .env
CAPTCHA_API_KEY=your_2captcha_api_key_here
VPN_LOCATION=best
HEADLESS=false
EOF
    echo "[✓] .env created. Please edit it and re-run setup if needed."
else
    echo "[✓] .env file detected."
fi

echo ">> Setup complete. You're ready to launch ReportRabbit with: python3 main.py"