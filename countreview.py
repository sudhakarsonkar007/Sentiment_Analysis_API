import pandas as pd
from sentimentscore import Get_Sentiment_Score
from formatoutput import Format_Output
from getreviews import Get_Review_Dataframe


def Count_Review(list):
    total_review=0
    pos_count=0
    neg_count=0
    neu_count=0
    for text in list:
        score=Get_Sentiment_Score(text)
        total_review += 1
        if score[0][0] > 0:
            pos_count += 1
        elif score[0][0] < 0:
            neg_count += 1
        else:
            neu_count += 1 
    sentiment_count=Format_Output(total_review,pos_count,neg_count,neu_count) 
    return sentiment_count


def Count_Text_Review(data):
    sentiment_count=Count_Review([data]) 
    return sentiment_count

    
def Count_Excel_Review(file):
    data_xls = pd.read_excel(file)
    list=data_xls['Reviews'].tolist()
    sentiment_count=Count_Review(list) 
    return sentiment_count

    
def Count_Product_Review(url):
    file = Get_Review_Dataframe(url)
    file.columns=['Reviews']
    list=file['Reviews'].values.tolist()
    sentiment_count=Count_Review(list) 
    return sentiment_count

