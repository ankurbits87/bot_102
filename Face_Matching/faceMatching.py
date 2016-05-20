import json
from pprint import pprint
import math
from datetime import datetime
import requests
import config

#url = "http://console.arya.ai/api/v2/faceMatch/query?access_token="+config.access_token+"&m_key="+config.m_key+"&app="+config.app_name
url = "http://console.arya.ai/api/v2/faceMatch/query?access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjIzMjY4NjI5OTg5MTF9.FuGVh4xJHlF7Yd6sPyybL55XdNN3aYBhi13BpWRvn3s&m_key=tejash_FM&app=TestChatBox"
#print url
headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json'}

bag_pos = {'similar', 'same', 'identical', 'like', 'related', 'matching', 'resembling', 'comparable'}
bag_neg = {'different', 'contrasting', 'distinct', 'mismatched', 'distant'}

pos_query = False   

def main():
    req = {}
    img1 = raw_input("Please enter the URL for the first image\n")
    img2 = raw_input("Please enter the URL for the second image\n")
    req["image1"] = img1
    req["image2"] = img2
    resp = {}
    try:
        data = json.dumps(req)
        pprint(data)
        response = requests.request("POST", url, data=data, headers=headers)
        query = raw_input("What is your question regarding the 2 images?")
        print "Query received properly"
        resp = response.json()
        print "JSON response formed properly"
    except Exception, e:
        print "Some error occured while forming the JSON request"
 
    if('success' in resp and resp['success']):    
        for pos in bag_pos:
            if pos in query:
                if 'not' in query or 'non' in query:
                    break
                pos_query = True
                if resp['identical']:
                    print "Yes, the two images are identical"
                else:
                    print "No, the two images are not identical"
        
        if(not pos_query):
            for neg in bag_neg:
                if neg in query:
                    if resp['identical']:
                        print "No, the two images are identical"
                    else:
                        print "Yes, the two images are not identical"

    else:
        print "Some error occured while sending the API request"
        pprint(resp)


if (__name__ == '__main__'):
    main()

