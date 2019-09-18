import generateToken
import helperModule
import flask
from flask import Flask
from flask import Request
from flask import Response
import json

# Global Variables
app = Flask(__name__)
accessToken = None
configData = None
expiresIn = None
expiresAt = None

@app.route("/",)
def index():
    return "Index!"

@app.route("/hello",methods=['POST'])
def hello():
    print (flask.request.values)
    print (flask.request.query_string)
    return "Hello World!"

@app.route("/members")
def members():
    return "Members"

@app.route("/getAllJourneys")
def getAllJourneys():
    generateToken.authorize()
    return json.dumps(helperModule.getJourneyList())

if __name__ == "__main__":
    generateToken.authorize()
    app.run(port=3000)

