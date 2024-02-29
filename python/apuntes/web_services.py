<<<<<<< HEAD
# --- API ---
"""
--- CODIGO DE EJEMPLO ---

import urllib.error, urllib.parse, urllib.request
import json
service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location:")
    if len(address) < 1: break
    url = service_url + urllib.parse.urlencode({"address": address})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not  in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
    """
    # --- API RATE LIMITING AND SECURITY ---
"""
los recursos par realizar/ejecutar estas APIS no son "gratis"
la info suele ser valiosa/utilizable, pude estar limitada las peticiones a cada dia,
pedir una API "key", o cobrar

descargar: https://www.py4e.com/code3/
           https://www.py4e.com/materials

 --- CODIGO DE EJEMPLO ---

import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = "https//api.twitter.com/1.1/friends/list.json"

while True:
    print(" ")
    acct = input("Enter twitter account:")
    if(len(acct) < 1): break
    url = twurl.argument(TWITTER_URL, {"screen name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js["users"]:
        print(u["screen_name"])
        s = u["status"]["text"]
        print("  ", s[:50])

=======
# --- API ---
"""
--- CODIGO DE EJEMPLO ---

import urllib.error, urllib.parse, urllib.request
import json
service_url = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location:")
    if len(address) < 1: break
    url = service_url + urllib.parse.urlencode({"address": address})

    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not  in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    location = js["results"][0]["formatted_address"]
    print(location)
    """
    # --- API RATE LIMITING AND SECURITY ---
"""
los recursos par realizar/ejecutar estas APIS no son "gratis"
la info suele ser valiosa/utilizable, pude estar limitada las peticiones a cada dia,
pedir una API "key", o cobrar

descargar: https://www.py4e.com/code3/
           https://www.py4e.com/materials

 --- CODIGO DE EJEMPLO ---

import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = "https//api.twitter.com/1.1/friends/list.json"

while True:
    print(" ")
    acct = input("Enter twitter account:")
    if(len(acct) < 1): break
    url = twurl.argument(TWITTER_URL, {"screen name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js["users"]:
        print(u["screen_name"])
        s = u["status"]["text"]
        print("  ", s[:50])

>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
"""