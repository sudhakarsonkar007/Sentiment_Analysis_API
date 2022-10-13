import pandas as pd
import numpy as np
import requests 
from bs4 import BeautifulSoup


headers = {
    'authority': 'www.amazon.in',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '0.8',
    'ect': '4g',
    'rtt': '0',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '0.8',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-viewport-width': '2400',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'service-worker-navigation-preload': 'true',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'viewport-width': '2400',
}


def Get_Soup(url):
    r = requests.get(url, headers=headers,
    params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


# Initialize list to store reviews data later on
reviewlist = []


# Function : look for web-tags in our soup, then append our data to reviewList

def Get_Reviews(soup):
    # reviewlist = []
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = item.find('span', {'data-hook': 'review-body'}).text.strip()
            reviewlist.append(review)
    except:
        pass
    

def Get_Url(productUrl):
    shortProductUrl = productUrl[0: productUrl.index("ref")]
    changeInUrl = shortProductUrl.replace("/dp/", "/product-reviews/")
    changeInUrl = shortProductUrl.replace("/gp/", "/product-reviews/")
    finalUrl = changeInUrl + \
    "ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    return finalUrl

# loop through :x many pages, or until the css selector found only on the last page is found (when the next page button is greyed) 
def Get_Review_Dataframe(productUrl):
    finalUrl=Get_Url(productUrl)
    for x in range(0, 10):
        soup = Get_Soup(finalUrl+'{x}')
        Get_Reviews(soup)
        if not soup.find('li', {'class': 'a-disabled a-last'}):
            pass
        else:
            break
        
    # Save results to a dataframe
    df = pd.DataFrame(reviewlist)
    df.replace("", np.NaN, inplace=True)
    df = df.dropna()
    return df
