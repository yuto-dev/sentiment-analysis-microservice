import pandas as pd
import base64
import requests
from datetime import date
import pandas as pd
import requests

alphaURL = "http://192.168.92.147:8000/"
betaURL = "http://192.168.92.145:8000/analyze/"

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



#---------- Call Gamma ---------------

# Replace these variables with your local WordPress site information
url = 'http://localhost/wp-json/wp/v2'
user = 'abi'
password = 'KwHj CRft wsoe L9yb VF4V JK7e'

wp_connection = user + ':' + password
token = base64.b64encode(wp_connection.encode())

headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

today = date.today().strftime("%y/%m/%d")

post_title = "Sentiment Analysis - " + today

post_body = insight

post = {'title': post_title,
            'status': 'publish',
            'content': post_body,
            'author': '1',
            'format': 'standard'
            }

wp_request = requests.post(url + '/posts', headers=headers, json=post)
print(wp_request)
