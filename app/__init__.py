from flask import Flask
from flask import Response
#init app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test", methods=['GET','POST'])
def response():
    return Response('',status=200)
