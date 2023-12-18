import requests
import praw

alphaURL = "http://192.168.92.144:8000/"
betaURL = "http://192.168.92.145:8000/analyze/"

#Call Alpha

# Initialize a Reddit API client
reddit = praw.Reddit(
    client_id='plTXW0WhFuIp3FEfXsFGGA',
    client_secret='AYYprYCHIhoOZd8sYS6YxIXHJtxC7g',
    user_agent='sentient-analysis',
)


# redditPostID = input("Enter a Reddit Post ID: ")

payload = []
payload = requests.get(alphaURL).json()

#---------- Call Beta ---------------


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
