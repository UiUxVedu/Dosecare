import requests

API_KEY = "PASTE_YOUR_API_KEY_HERE"

def send_sms(phone, message):
    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = {
        "message": message,
        "language": "english",
        "route": "q",
        "numbers": phone,
    }

    headers = {
        "authorization": API_KEY,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    print("SMS Response:", response.text)