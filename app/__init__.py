from flask import Flask
from flask import Response
from flask import request
from flask import json
import smartsheet

#init app
app = Flask(__name__)
ss_client = smartsheet.Smartsheet('l07xoamqp4rg0v9helj4talqy2')
print("I'm starting...")

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/test", methods=['GET','POST'])
def response():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        print(data)
        if data.challenge:
            return Response({"smartsheetHookResponse":data.challenge}, status=200)
    return Response('',status=200)

@app.route("/createwebhook")
def create_webhook():
    print("Creating webhook")
    Webhook = ss_client.Webhooks.create_webhook(
        ss_client.models.Webhook({
            'name':'Test Webhook',
            'callbackUrl':'https://smartsheettest.herokuapp.com/test',
            'scope':'sheet',
            'scopeObjectId': 7292894332643204,
            'events' : ['*.*'],
            'version': 1
        })
    )
