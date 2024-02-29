<<<<<<< HEAD
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# ignorar certificados de rror SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
# retrieve all of the anchor tags 
tags = soup('a')
for tag in tags:
=======
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# ignorar certificados de rror SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter -")
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup(html, "html.parser")
# retrieve all of the anchor tags 
tags = soup('a')
for tag in tags:
>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
    print(tag.get("href", None))