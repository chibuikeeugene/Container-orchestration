import os
import socket
import requests
from datetime import datetime

def main() -> None:
    """a basic python"""
    username = os.getenv("APP_USER", "Docker Student")

    print("Getting started with Docker...")
    print(f"Hello: {username}")
    print(f"Container hostname: {socket.gethostname()}")
    print(f"Current time: {datetime.now().isoformat()}")

    # fetch info from web
    url = os.getenv("TARGET_URL", "https://www.example.com")

    try:
        response = requests.get(url, timeout=10)
        print(f"URL: {url}")
        print(f"Status code: {response.status_code}")
        print(f"Content length: {len(response.content)} bytes")

    except requests.RequestException as e:
        print(f"The {e} error occured")

if __name__ == "__main__":
    main()