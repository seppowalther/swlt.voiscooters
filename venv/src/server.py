import requests
import time
from datetime import datetime as DateTime

def opensessionjson():
    opensessionjson= {
           "authenticationToken": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODI0NDQzNzUsImp0aSI6IjAiLCJpYXQiOjE1ODI0MDExNzUsImlzcyI6ImF1dGguYXBpLnZvaWFwcC5pbyIsIm5iZiI6MTU4MjQwMTE3NCwidXNlcklkIjoiZmUwZWFlOTktODMwYS00NjRlLWFjNGQtODQ1ZDNlMjY3ZDlhIiwiVXNlcklEIjoiZmUwZWFlOTktODMwYS00NjRlLWFjNGQtODQ1ZDNlMjY3ZDlhIiwiVmVyaWZpZWQiOmZhbHNlLCJ2ZXJpZmllZCI6ZmFsc2V9.CbsONbZ2YrpvzbrystJbV-oI8pg4SK-xiUt0tQlbMOc4D3n1dVDx_d5jVtoORmmpwHcj2rCR0qBhw0MgUoM4_Q"
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

