import requests
import base64
from datetime import date

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

def fetchPosts(sub):

    posts = []
    comments = []

    fetchURL = alphaURL + 'board/?sub=' + sub

    try:
        response = requests.get(fetchURL)
        posts = response.json()

    # Check the status code
    except requests.RequestException as e:
        print(f"An error occurred while fetching post IDs: {e}")
        
    return posts

def fetchComments(post):
    
    comments = []

    print(f"{bcolors.OKBLUE}Fetching comments from post with the ID " + post + f"...{bcolors.ENDC}")

    fetchURL = alphaURL + 'post/?post=' + post
    response = requests.get(fetchURL)

    comments = response.json()

    print(f"{bcolors.OKGREEN}Fetched " + str(len(comments)) + " comments" + f".{bcolors.ENDC}")
    print(comments[-1])
    return comments

def analyze(payload):

    fetchURL = betaURL
    response = requests.get(betaURL, json=payload)
    
    if response.status_code == 200:
        print(f"Request success! {bcolors.OKGREEN}(Status Code 200).{bcolors.ENDC}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

    response = response.json()
    response.pop(-1)
    responseFilter = [num for num in response if num != 0.0]
    response = responseFilter

    sum = 0
    for scores in response:
        sum = scores + sum
        
    average = sum / len(response)
    
    insight = format(average, '.4f')
    
    return insight

def publish(avgScore, subreddit):
    
    url = 'http://kayumeranti.my.id/wp-json/wp/v2'
    user = 'user'
    password = 'pass'

    wp_connection = user + ':' + password
    token = base64.b64encode(wp_connection.encode())

    headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

    today = date.today().strftime("%y/%m/%d")

    post_body = "Today on " + today + ", the average score of sentiment analysis ran on the comments of the top 10 posts of the subreddit r/" + subreddit + " is " + avgScore + "."

    post = {'title': avgScore,
            'status': 'publish',
            'content': post_body,
            'author': '1',
            'format': 'standard'
            }
    
    # Assuming you have tag names like 'tag1', 'tag2', etc.
    tag_names = []
    tag_names.append(subreddit)

    # Get tag IDs by querying the WordPress REST API for each tag
    tag_ids = []
    for tag_name in tag_names:
        tag_response = requests.get(url + '/tags', params={'search': tag_name}, headers=headers)
        tag_data = tag_response.json()
    
        if tag_response.status_code == 200 and tag_data:
            tag_ids.append(tag_data[0]['id'])
        else:
            # Handle the case where the tag doesn't exist or the request fails
            print(f"Error getting tag ID for '{tag_name}': {tag_response.content}")

    # Update the 'tags' field in the post dictionary with tag IDs
    post['tags'] = tag_ids

    wp_request = requests.post(url + '/posts', headers=headers, json=post)
    print(wp_request)
    print("Response Code:", wp_request.status_code)
    print("Response Content:", wp_request.content)


testSub = ["intel", "amd", "nvidia", "gaming", "pcgaming", "civ", "space", "cars", "rally", "jdm"]

for sub in testSub:
    
    postList = fetchPosts(sub)

    comments = fetchComments(postList[0])

    commentAverage = analyze(comments)

    publish(commentAverage, sub)
