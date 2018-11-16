import smartsheet
import re
import json
def create_webhook():
    ss_client = smartsheet.Smartsheet('l07xoamqp4rg0v9helj4talqy2')
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
    wh = Webhook.to_dict()
    print(wh)
    ss_client.Webhooks.update_webhook(wh['data']['id'],
    ss_client.models.Webhook({
        'enabled': True}))
    
create_webhook()