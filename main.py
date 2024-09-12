import flask
import json

print("Main.py starting the webserver!")

def responseMake(r):
    try:
        json.dumps(r)
    except:
        pass
    resp = flask.Response(json.dumps(r))
    resp.headers.add('Access-Control-Allow-Origin', "*")
    return resp

app = flask.Flask(__name__)

@app.route("/")
def home():
    return responseMake("Website is working, this is /"), 200


app.run(host="0.0.0.0", port=7777)