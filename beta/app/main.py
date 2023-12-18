from fastapi import FastAPI, Body
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = FastAPI()
analyzer = SentimentIntensityAnalyzer()

@app.get("/")
async def defaultReturn():
    string = "Hello World"
    return string
@app.get("/analyze/")
async def read_items(paragraphs: list[str] = Body(...)):

    items = []
    compound = []
    sum = 0

    for paragraph in paragraphs:
        print(paragraphs)
        score = analyzer.polarity_scores(paragraph)
        compound.append(score["compound"])

    for scores in compound:
        sum = scores + sum

    average = sum / len(compound)

    stringAverage = "The average score is " + format(average, '.4f')

    compound.append(stringAverage)

    #return {"paragraphs": items}
    return compound
