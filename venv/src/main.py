import requests

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
    for i in range(0, number):
        print(zones[i]['name'] + " (" + zones[i]['zone_id'] + ")")


def getscooternumber(accesstoken, zoneid):
    accesstoken = accesstoken
    getscooternumberresult = requests.get("https://api.voiapp.io/v1/vehicles/zone/"+zoneid+"/ready", headers=getzonesinfoheaders(accesstoken))
    getscooternumberdict = getscooternumberresult.json()

    # zones = getzonesinfodict.get("zones")

    number = len(getscooternumberdict)
    newnumber = 0

    for i in range(0, number):
        model = getscooternumberdict[i]['type']
        lastupdate = getscooternumberdict[i]['updated']
        if lastupdate.startswith('2020-02'):
            newnumber = newnumber + 1

    print("In der ausgewählten Stadt stehen gerade " + str(newnumber) + " Voi Scooter zur Ausleihe bereit.")
    # for i in range(0, number):
        # print(getscooterinfodict[i]['short'])

def getscootermodel(accesstoken, zoneid):
    accesstoken = accesstoken
    getscooternumberresult = requests.get("https://api.voiapp.io/v1/vehicles/zone/"+zoneid+"/ready", headers=getzonesinfoheaders(accesstoken))
    getscooternumberdict = getscooternumberresult.json()

    # zones = getzonesinfodict.get("zones")

    number = len(getscooternumberdict)
    list = []
    for i in range(0, number):
        model = getscooternumberdict[i]['type']
        lastupdate = getscooternumberdict[i]['updated']
        if model in list:
            pass
        else:
            if lastupdate.startswith('2020-02'):
                list.append(model)
    print(list)


def main():
    accesstoken = opensession()
    print("======================")
    print("Sie sehen gleich eine Liste mit den Städten, in denen Voi aktiv ist. Hinter dem Städtenamen befindet sich in Klammern die zugehörige Zone-ID.")
    print("Um Informationen über Roller im Voi-System abzufragen, wählen Sie bitte die gewünschte Stadt aus, indem Sie die Zone-ID eingeben.")
    print("Wenn Sie diese Information gelesen und verstanden haben, klicken Sie bitte ENTER um fortzufahren.")
    input()
    getzonesinfo(accesstoken)
    print("-----------------------")
    zoneid = input("Zone_ID eingeben: ")
    print("-----------------------")
    print("Super. Wofür interessieren Sie sich?")
    print("")
    print("Wie viele Roller stehen zur Verfügung? (1)")
    print("Welche Rollermodelle werden eingesetzt? (2)")
    print("")
    print("-----------------------")
    method = input("Auswahl eingeben: ")
    print("-----------------------")
    if method == "1":
        getscooternumber(accesstoken, zoneid)
    elif method == "2":
        getscootermodel(accesstoken, zoneid)

if __name__ == "__main__":
    main()
