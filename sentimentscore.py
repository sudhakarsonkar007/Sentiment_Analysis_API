from textblob import TextBlob

def Get_Sentiment_Score(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list
