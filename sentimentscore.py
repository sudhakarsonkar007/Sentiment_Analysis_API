from textblob import TextBlob

def get_sentiment_score(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list
