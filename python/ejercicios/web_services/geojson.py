<<<<<<< HEAD
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
=======
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
>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
    print(location)