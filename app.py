from datetime import date
from re import search
from flask import Flask, json, render_template, request
from elasticsearch import Elasticsearch


es = Elasticsearch()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/api/v1/cordinates', methods = ["GET","POST"])
def query_searching():
    index_tweet = 'tweets'
    topLong = request.form['minlatInput']
    topLat = request.form['maxlatInput']
    bottomLon = request.form['minlonInput']
    bottomLat = request.form['maxlonInput']
    body = {
        "query": {
            "multi_match": {
                "topRight": ["topLong", "topLat"],
                "BottomLeft": ["bottomLon", "bottomLat"]
            }
        }
    }
    
    search = es.search(index=index_tweet, body=body)
    dic = {}
    for i in search:
        date_time = search[0][1].split(0)
        if date_time in dic:
            dic[i] +=1
        else:
            dic[i]=1
    # search = [
    #     {
    #         "index":"name"
            
    #         "_sours":{
    #             "created_at":"20112-2-5"  ,
    #             "text": "oooo"
    #         }
    #     }
    # ]
    # dic = {
    #     "2012-12-12": 2,
    #     "222222":1
    # }
    
    # for i in search:
    #     if i['_sours']['date'] in dic:
    #         dic[i] +=1
    #     else:
    #         dic[i] = 1
    return render_template('tweets.html', x_name=dic.keys(), y_name=dic.values())

if __name__ == "__main__":
    app.run(debug=True)