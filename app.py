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
    results = es.get(index= index_tweet, doc_type='title')
    return jsonify(results['_source'])

@app.route('/api/v1/cordinates', methods = ["POST"] )
def query_searching():
    index_tweet = 'tweets'
    coordinates = request.form['coordinates']
    body = {
        "query": {
            "multi_match": {
                "fields": ["long", "lat"]
            }
        }
    }
    
    search = es.search(index=index_tweet, body=body)
    return jsonify(search['long']['lat'])


if __name__ == "__main__":
    app.run()