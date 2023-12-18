import requests

url = "http://127.0.0.1:8000/analyze/"

payload = ["You are so good!", "It's ok I guess", "Kill yourself faggot"]

response = requests.get(url, json=payload)

if response.status_code == 200:
    print("Success! Response:")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")

print(type(response))