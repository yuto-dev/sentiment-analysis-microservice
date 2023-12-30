from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import praw
import pandas as pd
import keys

app = FastAPI()

# Initialize a Reddit API client
reddit = praw.Reddit(
    client_id = keys.client_id,
    client_secret= keys.client_secret,
    user_agent= keys.user_agent
)

@app.get("/")
def defaultPost():
    # Get the post by its ID or URL
    submission = reddit.submission(id='okwyxe')

    # Create empty lists to store comment data
    comment_author = []
    comment_body = []
    comment_score = []

    # Iterate through the comments and collect data
    for comment in submission.comments:
        comment_author.append(comment.author.name if comment.author else "Deleted")
        comment_body.append(comment.body)
        comment_score.append(comment.score)

    # Create a DataFrame
    comments_data = pd.DataFrame({
        'Author': comment_author,
        'Body': comment_body,
        'Score': comment_score,
    })

    return comment_body

@app.get("/post/")
def queryPost(post: str):
    # Get the post by its ID or URL
    submission = reddit.submission(id = post)

    # Create empty lists to store comment data
    comment_author = []
    comment_body = []
    comment_score = []

    # Iterate through the comments and collect data
    for comment in submission.comments:
        comment_author.append(comment.author.name if comment.author else "Deleted")
        comment_body.append(comment.body)
        comment_score.append(comment.score)

    # Create a DataFrame
    comments_data = pd.DataFrame({
        'Author': comment_author,
        'Body': comment_body,
        'Score': comment_score,
    })

    return comment_body

@app.get("/board/")
def querySub(sub: str):
    # Get the subreddit instance
    subreddit = reddit.subreddit(sub)

    # Get the top posts of the day
    top_posts = subreddit.top(time_filter='day', limit=10)

    # Extract post IDs
    post_ids = [post.id for post in top_posts]

    return post_ids


