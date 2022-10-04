from re import T
import flask_excel as ex
from flask import request
from typing import OrderedDict
from flask import Flask,request
from countreview import count_text_review,count_excel_review

app= Flask(__name__)

#new branch for sudhakar


@app.route('/sentiment', methods=['GET', 'POST'])
def get():
    content_type=request.headers.get('content-type')
    if(content_type=='application/json'):
        data = request.get_json() 
        result=count_text_review(data)
    else:
        f = request.files['file_key']
        result=count_excel_review(f)

    return OrderedDict(result)



if __name__ == "__main__":
    app.run(debug="TRUE")
        
