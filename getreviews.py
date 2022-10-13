import pandas as pd
import numpy as np
import requests 
from bs4 import BeautifulSoup
from header import headers


def Get_Soup(url):
    r = requests.get(url, headers=headers,
    params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def Get_Reviews(soup):
    reviewlist = []
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = item.find('span', {'data-hook': 'review-body'}).text.strip()
            reviewlist.append(review)
    except:
        pass
    return reviewlist


def Get_Url(productUrl):
    shortProductUrl = productUrl[0: productUrl.index("ref")]
    changeInUrl = shortProductUrl.replace("/dp/", "/product-reviews/")
    changeInUrl = shortProductUrl.replace("/gp/", "/product-reviews/")
    finalUrl = changeInUrl + \
    "ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=avp_only_reviews&sortBy=recent&pageNumber=1&filterByStar=one_star&pageNumber="
    return finalUrl

# loop through :x many pages, or until the css selector found only on the last page is found (when the next page button is greyed) 
def Get_Review_Dataframe(productUrl):
    reviewlist=[]
    finalUrl=Get_Url(productUrl)
    for x in range(0, 10):
        soup = Get_Soup(finalUrl+'{x}')
        review=Get_Reviews(soup)
        reviewlist.extend(review)
        if not soup.find('li', {'class': 'a-disabled a-last'}):
            pass
        else:
            break
    df = pd.DataFrame(reviewlist)
    df.replace("", np.NaN, inplace=True)
    df = df.dropna()
    return df
