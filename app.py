from re import search
from flask import Flask, json, render_template,jsonify,request
from elasticsearch import Elasticsearch

es = Elasticsearch()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/api/v1/cordinates', methods=["GET"])
def index():
    index_tweet = 'tweets'
    results = es.get(index = index_tweet, doc_type='title')
    return  render_template('main.html', tweets=results)

@app.route('/api/v1/cordinates', methods = ["POST"] )
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

    return  render_template('main.html', tweets=search)

if __name__ == "__main__":
    app.run(debug=True)