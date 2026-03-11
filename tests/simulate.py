import requests
import time

BASE_URL = "http://127.0.0.1:8000"

print("Step 1: Sending 10 Normal Requests...")
for _ in range(10):
    requests.get(BASE_URL)
    time.sleep(1)

print("Step 2: Sending a 'Ghost' Anomaly (Large payload, zero gap)...")
requests.post(BASE_URL, data="HACK"*250) 

print(f"Step 3: Check http://127.0.0.1:8000/analyze to see the -1 Noise point!")