import json
import requests
import mainModule
from datetime import datetime, timedelta
import generateToken

def getContentsList():
    configData = mainModule.configData
    # extracting accesstoken and expiryTime
    accessToken = mainModule.accessToken
    ##########
    newRequestBody = {
                        "page":
                        {
                            "page":1,
                            "pageSize":200
                        },

                        "query":
                        {
                            "leftOperand":
                            {
                                "property":"assetType.id",
                                "simpleOperator":"greaterThanOrEqual",
                                "value":16
                            },
                            "logicalOperator":"AND",
                            "rightOperand":
                            {
                                "property":"assetType.id",
                                "simpleOperator":"lessThanOrEqual",
                                "value":74
                            }
                        }
                    }

    newRequestHeader = {
        "Authorization":"Bearer "+accessToken,
        "Content-Type": "application/json"
    }

    r2 = requests.post(url = configData['authURLs']['restBaseURL']+'/asset/v1/content/assets/query',headers=newRequestHeader,json = newRequestBody)

    # extracting data in json format
    outputJSON = r2.json()

    return outputJSON

def getContent(newRequestId):
    configData = mainModule.configData
    # extracting accesstoken and expiryTime
    accessToken = mainModule.accessToken

    newRequestHeader = {
        "Authorization":"Bearer "+accessToken,
        "Content-Type": "application/json"
    }

    r2 = requests.get(url = configData['authURLs']['restBaseURL']+'/asset/v1/content/assets/'+newRequestId,headers=newRequestHeader)

    # extracting data in json format
    outputJSON = r2.json()

    return outputJSON

def getJourneyList():
    configData = mainModule.configData
    # extracting accesstoken and expiryTime
    accessToken = mainModule.accessToken
    newRequestHeader = {
        "Authorization":"Bearer "+accessToken,
        "Content-Type": "application/json"
    }

    r2 = requests.get(url = configData['authURLs']['restBaseURL']+'/interaction/v1/interactions',headers=newRequestHeader)

    # extracting data in json format
    outputJSON = r2.json()

    jList = outputJSON['items']
    finalJourneyData = {}
    print(jList)
    for j in jList:
        finalJourneyData[j['name']+'_'+j['id']] = getJourneyData(j['id'])
    print("Expires in: "+str(mainModule.expiresIn))
    return finalJourneyData

def getJourneyData(journeyId):
    if((datetime.now() - timedelta(seconds=5))>mainModule.expiresAt):
        print("If in")
        generateToken.authorize()
    else:
        print("else")
    configData = mainModule.configData
    # extracting accesstoken and expiryTime
    accessToken = mainModule.accessToken
    newRequestHeader = {
        "Authorization":"Bearer "+accessToken,
        "Content-Type": "application/json"
    }
    r2 = requests.get(url = configData['authURLs']['restBaseURL']+'/interaction/v1/interactions/'+journeyId,headers=newRequestHeader)

    # extracting data in json format
    outputJSON = r2.json()
    return outputJSON
