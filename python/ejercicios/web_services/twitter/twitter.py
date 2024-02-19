import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl
import json

# create app and get four strings, put them in hidden.py
"""
--- PRIMER EJEMPLO ---
print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'count' : '2'})

print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connection = urllib.request.urlopen(url, context = ctx)
data = connection.read()
print(data)
print("=====================")

headers = dict(connection.getheaders())
print(headers)
"""
"""
--- SEGUNDO EMJEMPLO ---
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json', {'screen_name': 'drchuck', 'count' : '2'})

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print(" ")
    acct = input("Enter twitter account:")
    if(len(acct) < 1): break
    url = twurl.argument(TWITTER_URL, {"screen name": acct, "count": "2"})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    print(data[:250])

    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])
"""
"""
--- TERCER EJMPLO ---

"""
TWITTER_URL = "https//api.twitter.com/1.1/friends/list.json"

while True:
    print(" ")
    acct = input("Enter twitter account:")
    if(len(acct) < 1): break
    url = twurl.argument(TWITTER_URL, {"screen name": acct, "count": "5"})
    print("Retrieving", url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()

    js = json.loads(data)
    print(json.dumps(js, indent=2))

    headers = dict(connection.getheaders())
    print("Remaining", headers["x-rate-limit-remaining"])

    for u in js["users"]:
        print(u["screen_name"])
        if'status' not in u:
            print("  * Not status found")
            continue
        s = u["status"]["text"]
        print("  ", s[:50])
   