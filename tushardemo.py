from nocache import nocache
from flask import send_file
from flask import Flask, request
import urllib
import wget
import requests, json
import uuid
import os
import sendgrid
import sys
from PIL import Image
###
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

# json_key = json.load(open('sendgrid-demo-4f4aedce75b2.json'))
# scope = ['https://spreadsheets.google.com/feeds']

# credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

# gc = gspread.authorize(credentials)

# wks = gc.open("Customer Data").sheet1

# wks.update_acell('B2', "it's down there somewhere, let me take another look.")

###

app = Flask(__name__)

API_USER = "tusharb"
API_KEY = "kenshi123"
NGROK_URL = "http://cefa38f0.ngrok.io"


@app.route ('/speak', methods=['POST'])
def demo():
    #get email info from SendGrid 
    subject = request.form['subject']
    to = request.form['from']

    #speak sent in subject
    cmd = "osascript -e 'say \""+subject+"\" using \"Junior\"'"
    os.system(cmd)
    
    #send magic message back to user talking about prizes
    sg = sendgrid.SendGridClient(API_USER, API_KEY)

    # construct the message
    message = sendgrid.Mail()
    
    message.add_substitution(':name', to)
    message.add_to(to)
    message.set_subject('Hello from SendGrid!')
    message.set_html('<b>Thank you for stopping by our booth!</b>')
    message.set_text('Thank you for stopping by our booth!!')
    message.set_from('SendGrid <hello@googlenext.bymail.in')
    

    # choose the appropriate template
    if subject=="gcp" or subject =="GCP" or subject=="Gcp":
        message.add_filter('templates', 'enable', '1')
        message.add_filter('templates', 'template_id', '0f057d74-6d22-414a-bf2b-964d4781c3b9')
        # wks.update_acell()

    else:
        message.add_filter('templates', 'enable', '1')
        message.add_filter('templates', 'template_id', 'c66f3398-090c-49e9-963d-6b4754b72e78')
        

    # send the message!
    status, msg = sg.send(message)
    print status, msg

    # need to return this to confirm receipt 
    return "OK"


if __name__=='__main__':
    app.run(debug=True)
