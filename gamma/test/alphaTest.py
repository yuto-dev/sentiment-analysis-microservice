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

output = []

# Stage 1

url = 'http://192.168.92.147:8000/'

# Make the GET request and notify the user
try:
    # Make the GET request
    response = requests.get(url)

    data = response.json()
    output.append(data[0])

    # Check the status code
    if response.status_code == 200:
        print(f"Stage 1 request was successful {bcolors.OKGREEN}(Status Code 200).{bcolors.ENDC}")
    else:
        print(f"Request failed with status code: {response.status_code}. Something might be wrong.")

except requests.RequestException as e:
    print(f"An error occurred in stage 1: {e}")

# Stage 2

sub = "kappachino"
url = 'http://192.168.92.147:8000/board/?sub=' + sub

try:
    # Make the GET request
    response = requests.get(url)

    data = response.json()
    output.append(data[0])

    # Check the status code
    if response.status_code == 200:
        print(f"Stage 2 request was successful {bcolors.OKGREEN}(Status Code 200).{bcolors.ENDC}")
    else:
        print(f"Request failed with status code: {response.status_code}. Something might be wrong.")

except requests.RequestException as e:
    print(f"An error occurred in stage 2: {e}")

# Stage 3

postID = data[0]
url = 'http://192.168.92.147:8000/post/?post=' + postID

try:
    # Make the GET request
    response = requests.get(url)

    data = response.json()
    output.append(data[0])

    # Check the status code
    if response.status_code == 200:
        print(f"Stage 3 request was successful {bcolors.OKGREEN}(Status Code 200).{bcolors.ENDC}")
    else:
        print(f"Request failed with status code: {response.status_code}. Something might be wrong.")

except requests.RequestException as e:
    print(f"An error occurred in stage 3: {e}")

print(output)
