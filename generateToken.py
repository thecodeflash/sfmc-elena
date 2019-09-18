import json
import requests
import mainModule
from datetime import datetime, timedelta

def authorize():
    with open('./config.json', 'r') as f:
        configData = json.load(f)

    # api-endpoint
    authURL = configData['authURLs']['authBaseURL']

    # defining a params dict for the parameters to be sent to the API
    jdata = configData['authData']

    requestHeader = {
        "Content-Type": "application/json"
    }

    # sending get request and saving the response as response object
    r = requests.post(url = authURL+'/v2/token', json = jdata, headers=requestHeader)

    print(r.status_code)
    # extracting data in json format
    data = r.json()


    # extracting accesstoken and expiryTime
    accessToken = data['access_token']

    expiresIn = data['expires_in']
    mainModule.expiresIn=expiresIn
    mainModule.expiresAt = datetime.now() + timedelta(seconds=expiresIn)
    mainModule.accessToken=accessToken
    mainModule.configData = configData
    return {
        'accessToken':accessToken,
        "expiresIn":expiresIn,
        "expiresAt":mainModule.expiresAt,
        'configData':configData}