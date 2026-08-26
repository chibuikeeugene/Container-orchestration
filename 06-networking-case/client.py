# a basic web request 

import os
import requests

server = os.getenv("SERVER-URL", "http://web-server")

response = requests.get(server, timeout=10)

print(f"Server: {server}")
print(f"Status: {response.status_code}")
print(response.text[:100])