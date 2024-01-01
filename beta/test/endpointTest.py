import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

url = "http://127.0.0.1:8000/analyze/"

payload = ["You are so good!", "It's ok I guess", "Kill yourself"]

response = requests.get(url, json=payload)

if response.status_code == 200:
    print(f"Sentiment analysis request was successful. {bcolors.OKGREEN}(Status Code 200){bcolors.ENDC}")
else:
    print(f"Request failed with status code: {response.status_code}. Something might be wrong.")