#!/bin/bash
echo ""
echo "  ================================"
echo "   STORYBOARD ENGINE v10.3"
echo "   Starting up... please wait"
echo "  ================================"
echo ""

# Go to the folder where this script lives
cd "$(dirname "$0")"

# Check if Python exists
if ! command -v python3 &> /dev/null; then
    echo "  ERROR: Python is not installed!"
    echo ""
    echo "  1. Go to https://python.org"
    echo "  2. Download and install Python"
    echo "  3. Double-click this file again"
    echo ""
    read -p "  Press Enter to close..."
    exit 1
fi

# Install dependencies if needed
echo "  Installing dependencies..."
pip3 install -r requirements.txt > /dev/null 2>&1
pip3 install pywebview > /dev/null 2>&1
echo "  Done!"
echo ""

# Launch the app
echo "  Opening the engine..."
echo "  (Close this terminal to stop the app)"
echo ""
python3 desktop.py
