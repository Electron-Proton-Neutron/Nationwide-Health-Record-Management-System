import random
import requests

# Generate OTP
otp = random.randint(112233, 988779)

# Define URL and headers
url = f"https://cpaas.messagecentral.com/verification/v3/send"
params = {
    "countryCode": "91",
    "customerId": "C-BCE9A5D99FF34D8",
    "senderId": "UTOMOB",
    "type": "SMS",
    "flowType": "SMS",
    "mobileNumber": "8353965282",
    "message": f"Your one-time password is {otp}",
}
headers = {
    "authToken": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJDLUJDRTlBNUQ5OUZGMzREOCIsImlhdCI6MTczNDg0MTQ5MiwiZXhwIjoxODkyNTIxNDkyfQ.kZGu-it47xo3XAHzywMzHQT4QR-s1-VlgMSA5FWYXlyhcvXtHYvJQj8tD5124uKuCfrpwfkjuLdiQopz1jgKuQ"
}

# Make POST request
response = requests.post(url, headers=headers, params=params)

# Debugging output
print(f"OTP: {otp}")
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")