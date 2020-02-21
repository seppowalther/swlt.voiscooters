import requests
import time
from datetime import datetime as DateTime

def opensessionjson():
    opensessionjson= {
           "authenticationToken": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODk4MDIyNDMsImp0aSI6IjAiLCJpYXQiOjE1ODIwMjYyNDMsImlzcyI6ImF1dGguYXBpLnZvaWFwcC5pbyIsIm5iZiI6MTU4MjAyNjI0MiwidXNlcklkIjoiOTVlMzllZjktMGU0NC00NWMzLTgwYjYtNDAyZTVmZDA5NTBlIiwiVXNlcklEIjoiOTVlMzllZjktMGU0NC00NWMzLTgwYjYtNDAyZTVmZDA5NTBlIiwiVmVyaWZpZWQiOmZhbHNlLCJ2ZXJpZmllZCI6ZmFsc2V9.SQ0QDXScHKSHGFSBGEAnYx8TmatOFiHHm5gQWlZzlgzl-xh0HOW0KawIquWARkCl_L8QjqTzIBbE2MUi2i7O0A"
        }
    return opensessionjson

def getzonesinfoheaders(accesstoken):
    getzonesinfoheaders = {
        'x-access-token': accesstoken
    }
    return getzonesinfoheaders

def opensession():
    opensessionresult = requests.post("https://api.voiapp.io/v1/auth/session", json=opensessionjson())
    opensessionresultdict = opensessionresult.json()
    accesstoken = opensessionresultdict.get("accessToken")
    return accesstoken

def getzonesinfo(accesstoken):
    accesstoken = accesstoken
    getzonesinforesult = requests.get("https://api.voiapp.io/v1/zones", headers=getzonesinfoheaders(accesstoken))
    getzonesinfodict = getzonesinforesult.json()
    zones = getzonesinfodict.get("zones")
    number = len(zones)

def getscooterinfo(accesstoken, zoneid):
    accesstoken = accesstoken
    getscooterinforesult = requests.get("https://api.voiapp.io/v1/vehicles/zone/"+zoneid+"/ready", headers=getzonesinfoheaders(accesstoken))
    getscooterinfodict = getscooterinforesult.json()

    # zones = getzonesinfodict.get("zones")

    number = len(getscooterinfodict)
    print(DateTime.now().strftime('%H:%M:%S')+" --> "+str(number))
    file = open('../../../../Downloads/statistik.txt', 'a')
    file.write(DateTime.now().strftime('%H:%M:%S')+" --> "+str(number))
    file.write("\n")
    file.close()
    # for i in range(0, number):
        # print(getscooterinfodict[i]['short'])

def main():
    while(1):
        accesstoken = opensession()
        getzonesinfo(accesstoken)
        zoneid = "169"
        getscooterinfo(accesstoken, zoneid)
        time.sleep(60)

if __name__ == "__main__":
    main()

