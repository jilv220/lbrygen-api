import flask
import requests
import os

from flask import request, jsonify
from flask_cors import CORS, cross_origin

# config flask
app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

# api 
@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/search', methods=['GET'])
def api_all():

    tag = request.args.get("t")
    #print(tag)

    claim_search = requests.post("http://localhost:5279", 
        json={  "method": "claim_search", 
                "params": {"any_tags": [str(tag)]}   }
        ).json()
    
    #print(type(claim_search))
    #print(claim_search.keys())
    
    return claim_search

@app.route('/api/getStream', methods=['GET'])
def get_stream_from_url():

    uri = request.args.get("url")
    print(uri)

    lbry_get = requests.post("http://localhost:5279", 
        json={  "method": "get", 
                "params": {"uri": str(uri)}   }
        ).json()
    
    #print(lbry_get)

    streaming_url = lbry_get["result"]["streaming_url"]
    #print(streaming_url)

    return streaming_url

app.run()