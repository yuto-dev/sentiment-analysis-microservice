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

alphaURL = "http://192.168.92.147:8000/"
betaURL = "http://192.168.92.145:8000/analyze/"

payload = []
output = []
payload = requests.get(alphaURL).json()


sub = "kappachino"
url = alphaURL + 'board/?sub=' + sub

try:
    # Make the GET request
    response = requests.get(url)

    # Returns post IDs
    data = response.json()

    # Check the status code

except requests.RequestException as e:
    print(f"An error occurred while fetching IDs: {e}")

comments = []
for post in data:

    url = alphaURL + 'post/?post=' + post
    response = requests.get(url)

    comments = response.json()
    payload.extend(comments)

print(comments)
#---------- Call Beta ---------------

'''
response = requests.get(betaURL, json=payload)

if response.status_code == 200:
    print("Success! Response:")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")

response = response.json()

print(type(response))

insight = response[-1]
print(insight)
'''