import flask
from flask import Response
import json
import subprocess
from accounts import api as accountsAPI

print("Main.py starting the webserver!")

def responseMake(r):
    try:
        json.dumps(r)
    except:
        pass
    resp = flask.Response(json.dumps(r))
    resp.headers.add('Access-Control-Allow-Origin', "*")
    return resp

# https://stackoverflow.com/questions/24578330/flask-how-to-serve-static-html
# sendStaticHTML("html/index.html") # Dont use "static/" for leading
def sendStaticHTML(filePath):
    return flask.current_app.send_static_file(filePath)

app = flask.Flask(__name__)

@app.route("/")
def home():
    return sendStaticHTML("html/index.html")
    #return responseMake("Website is working, this is /"), 200

@app.route("/ngrok")
def getNgrokTunnels():
    command = "ngrok api tunnels list"
    try:
        pullOutput = subprocess.check_output(command, shell=True, text=True)
    except:
        pullOutput = "{}"
        
    pullOutput = json.loads(pullOutput)
    
    return flask.jsonify(pullOutput), 200
    #return responseMake(pullOutput), 200

@app.route("/status/cpu")
def getCpuUsage():
    command = "mpstat -P ALL"
    try:
        pullOutput = subprocess.check_output(command, shell=True, text=True)
    except:
        pullOutput = f"Failed executing command ({command})"
    
    return pullOutput, 200


@app.route("/api/signup")
def signup():
    return accountsAPI.signup()



app.run(host="0.0.0.0", port=7777)