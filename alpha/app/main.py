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
    client_secret = keys.client_secret,
    user_agent = keys.user_agent,
)

@app.get("/")
def defaultPost():
    # Get the post by its ID or URL
    submission = reddit.submission(id='17zmop9')

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

@app.get("/pull/")
def queryPost(post: str):
    # Get the post by its ID or URL
    submission = reddit.submission(id=post)

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

