"""
STORYBOARD VISUAL ENGINE v10.3 — Desktop Launcher
Runs the engine as a native desktop window.

Usage:
    python desktop.py

Requirements (one-time):
    pip install -r requirements.txt
    pip install pywebview

If pywebview is not installed, falls back to opening in your default browser.
"""

import sys
import os
import threading
import time
import socket

def find_free_port():
    """Find a free port on localhost."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

def wait_for_server(port, timeout=15):
    """Wait until the Flask server is accepting connections."""
    start = time.time()
    while time.time() - start < timeout:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.3)
    return False

def start_flask(port):
    """Start the Flask app on the given port."""
    # Suppress Flask dev server banner noise
    import logging
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.WARNING)

    from app import app
    app.run(host="127.0.0.1", port=port, debug=False, use_reloader=False)

def main():
    port = find_free_port()
    url = f"http://127.0.0.1:{port}"

    # Start Flask in a background thread
    server_thread = threading.Thread(target=start_flask, args=(port,), daemon=True)
    server_thread.start()

    print(f"Starting Storyboard Engine v10.3 on {url} ...")

    if not wait_for_server(port):
        print("ERROR: Server failed to start within 15 seconds.")
        sys.exit(1)

    print("Server ready.")

    # Try native desktop window via pywebview
    try:
        import webview

        window = webview.create_window(
            "STORYBOARD VISUAL ENGINE v10.3",
            url,
            width=1400,
            height=900,
            min_size=(900, 600),
            text_select=True,
        )
        webview.start(debug=False)

    except ImportError:
        # Fallback: open in default browser
        print("pywebview not installed — opening in browser instead.")
        print("(Install it for a native window: pip install pywebview)")
        import webbrowser
        webbrowser.open(url)

        # Keep the server alive
        try:
            print(f"\nEngine running at {url}")
            print("Press Ctrl+C to stop.\n")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nShutting down.")

if __name__ == "__main__":
    main()
