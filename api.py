from fastapi import FastAPI
from utils import get_sentiment

app = FastAPI(debug=True)


@app.post('/emotion')
def get_emotion(user_pormpt: str):
    sentiment = get_sentiment(user_pormpt=user_pormpt)
    return sentiment
