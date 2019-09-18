import json
import requests

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

##########
newRequestBody = {
                    "page":
                    {
                        "page":2,
                        "pageSize":10
                    }
                    # ,

                    # "query":
                    # {
                    #     "leftOperand":
                    #     {
                    #         "property":"assetType.id",
                    #         "simpleOperator":"greaterThanOrEqual",
                    #         "value":16
                    #     },
                    #     "logicalOperator":"AND",
                    #     "rightOperand":
                    #     {
                    #         "property":"assetType.id",
                    #         "simpleOperator":"lessThanOrEqual",
                    #         "value":74
                    #     }
                    # }
                }

newRequestHeader = {
    "Authorization":"Bearer "+accessToken,
    "Content-Type": "application/json"
}

r2 = requests.post(url = configData['authURLs']['restBaseURL']+'/asset/v1/content/assets/query',headers=newRequestHeader,json = newRequestBody)

# extracting data in json format
data = r2.json()

print(r2)

with open('./outputs/ContentList.json', 'w') as outfile:
    json.dump(data, outfile)


