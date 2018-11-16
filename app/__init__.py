from flask import Flask
from flask import Response
from flask import request
from flask import json
from flask import jsonify
import smartsheet

#init app
app = Flask(__name__)
ss_client = smartsheet.Smartsheet('l07xoamqp4rg0v9helj4talqy2')
print("I'm starting...")

@app.route("/")
def hello():
    print("hello hello")
    return "Hello world!"

@app.route("/test", methods=['GET','POST'])
def response():
    print(request.headers['Content-Type'])
    print(request.headers)
    if 'application/json' in request.headers['Content-Type']
        print("json type")
        print(request)
        print(dir(request))
        data = request.get_json()
        print(dir(data))
        print(data)
        if data.get('challenge',None):
            print("found a challenge attribute")
            return jsonify({"smartsheetHookResponse":data['challenge']})
        else:
            print(data)
            return Response('', status=200)
    else:
        print("no json")
        return Response('tested!',status=200)

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
    wh = json.loads(Webhook)
    print(wh)
    ss_client.Webhooks.update_webhook(wh.id_,
    ss_client.models.Webhook({
        'enabled': True}))
    return "maybe all good"