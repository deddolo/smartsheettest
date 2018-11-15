from flask import Flask
from flask import Response
import smartsheet
#init app
app = Flask(__name__)
ss_client = smartsheet.Smartsheet('l07xoamqp4rg0v9helj4talqy2')

print("I'm starting...")
@app.route("/")
def hello():
    user_profile = ss_client.Users.get_current_user()
    return json.dumps(user_profile)

@app.route("/test", methods=['GET','POST'])
def response():
    return Response('',status=200)

@app.route("/createwebhook")
def create_webhook():
