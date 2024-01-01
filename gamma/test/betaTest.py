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

betaURL = "http://192.168.92.145:8000/analyze/"

payload = ["You are so good!", "It's ok I guess", "Kill yourself"]

#---------- Call Beta ---------------


response = requests.get(betaURL, json=payload)

if response.status_code == 200:
    print(f"Request success! {bcolors.OKGREEN}(Status Code 200).{bcolors.ENDC}")
    print("Request:")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")

response = response.json()


insight = response[-1]
print(insight)
