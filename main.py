import requests
import time

# Define the request URL
url = "https://api.monkeyrush.fun/api/v1/game/tap"

# Define the headers
headers = {
    "Authorization": "Bearer dXNlcj0lN0IlMjJpZCUyMiUzQTE1NjUyODU1NjQlMkMlMjJmaXJzdF9uYW1lJTIyJTNBJTIyJUU2JUIwJTk0REFSVE9OJUU0JUI5JTg4JTIyJTJDJTIybGFzdF9uYW1lJTIyJTNBJTIyJTIyJTJDJTIydXNlcm5hbWUlMjIlM0ElMjJEYXJ0b25UViUyMiUyQyUyMmxhbmd1YWdlX2NvZGUlMjIlM0ElMjJlbiUyMiUyQyUyMmFsbG93c193cml0ZV90b19wbSUyMiUzQXRydWUlMkMlMjJwaG90b191cmwlMjIlM0ElMjJodHRwcyUzQSU1QyUyRiU1QyUyRnQubWUlNUMlMkZpJTVDJTJGdXNlcnBpYyU1QyUyRjMyMCU1QyUyRml5M0hwMENkSW82bVphWWZpODNFSGQ3aDJuUHlYRzFGZDVWNTAtU2tEMkkuc3ZnJTIyJTdEJmNoYXRfaW5zdGFuY2U9LTcxMjQ5MjgwMDc4OTg0NTM5NTImY2hhdF90eXBlPXNlbmRlciZhdXRoX2RhdGU9MTc0MDI0MzQ2NiZzaWduYXR1cmU9SmdFNjlPTnJlYlphckJpSW1Kc3BDcVhEM1B2eDJPVG5QZVNPZjFRdU8tXzdwNEdUbkp6Y1VPeEVIQ2xqb21xaFR4dWdBdUctV0ItSWNJNU9mY0ktQXcmaGFzaD1hOGYwZDBiYzI4MDQ0OTA3NTE1YTA1N2VmOTI4ZmZhMGE4OTE2MDdkOGQ2ZjQ2YThlYTFhZTViY2Y1Y2RhNzc2",
    "Content-Type": "application/json",
    "Origin": "https://clicker.monkeyrush.fun",
    "Referer": "https://clicker.monkeyrush.fun/",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36"
}

# Define the request payload with updated score
payload = {
    "score": 500  # Updated score value
}

# Function to send the POST request
def send_request():
    try:
        response = requests.post(url, headers=headers, json=payload)
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except Exception as e:
        print(f"An error occurred: {e}")

# Infinite loop to send the request every 180 seconds
while True:
    send_request()
    
    # Countdown for 100 seconds
    sleep_time = 100
    while sleep_time > 0:
        print(f"Next request in {sleep_time} seconds", end="\r")
        time.sleep(1)
        sleep_time -= 1