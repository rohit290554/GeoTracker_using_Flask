import socket

import flask
from flask import Flask, jsonify, request
import requests
import json
import urllib.request

app = Flask(__name__)


@app.route('/', methods=["GET"])
# Initialize Nominatim API
def geotracker():
    ipur = 'https://ipapi.co/'
    ipurr = '/json/'
    external_ip  = ip_address = flask.request.remote_addr
    '''urllib.request.urlopen('https://ident.me').read().decode('utf8')
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')'''
    print('Target IP Addr is : ' + external_ip)
    ip_address = external_ip
    # URL to send the request to
    request_url = ipur + external_ip + ipurr
    # Send request and decode the result
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    test = json.dumps(result)
    return test

'''
    try:
        for key, value in result.items():
            return key, ' : ', value
    except:
        return 'Error'
'''
