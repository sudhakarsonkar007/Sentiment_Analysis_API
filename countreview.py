import pandas as pd
from sentimentscore import get_sentiment_score
from formatoutput import formatoutput


def count_text_review(data):
    total_review=0
    pos_count=0
    neg_count=0
    neu_count=0
    score=get_sentiment_score(data)
    total_review += 1
    if score[0][0] > 0:
        pos_count += 1
    elif score[0][0] < 0:
        neg_count += 1
    else:
        neu_count += 1  
    count=formatoutput(total_review,pos_count,neg_count,neu_count)
    return count


def count_excel_review(file):
    data_xls = pd.read_excel(file)
    list=data_xls['Reviews'].tolist()
    total_review=0
    pos_count=0
    neg_count=0
    neu_count=0
    for text in list:
        score=get_sentiment_score(text)
        total_review += 1
        if score[0][0] > 0:
            pos_count += 1
        elif score[0][0] < 0:
            neg_count += 1
        else:
            neu_count += 1  
                 
    count=formatoutput(total_review,pos_count,neg_count,neu_count)
    return count