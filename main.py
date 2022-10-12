from re import T
import flask_excel as ex
from flask import request
from typing import OrderedDict
from flask import Flask,request
from countreview import Count_Text_Review, Count_Excel_Review, Count_Product_Review

app= Flask(__name__)


@app.route('/sentiment', methods=['GET', 'POST'])
def Get():
    content_type=request.headers.get('content-type')
    if(content_type=='application/json'):
        data = request.get_json() 
        result=Count_Text_Review(data)
    else:
        f = request.files['file_key']
        result=Count_Excel_Review(f)

    return OrderedDict(result)


@app.route('/product_sentiments', methods=['GET', 'POST'])
def Get_Review():
    url = request.get_json() 
    result=Count_Product_Review(url)
    
    return OrderedDict(result) 


if __name__ == "__main__":
    app.run(debug="TRUE")
        
