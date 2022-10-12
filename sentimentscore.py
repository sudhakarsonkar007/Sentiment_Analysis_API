from textblob import TextBlob

def review(data):
    feedback=data
    blob=TextBlob(feedback)
    list=[]
    list.append(blob.sentiment)
    return list
