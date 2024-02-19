
"""
sockets: (TCP)
import socket
mysock:  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect("data.pr4e.org", 80) - "mysock.connect("host", "port")"

- APLICATION PROTOCOL: Mail, www
protoclo http: recupera HTML, imagenes, documentos...
               conjunto de reglas q permiten a los navegador para recuperar documentos web de servidores en internet
"http://www.dr-chuck.com/page1.htm" - "protocol"_"host"_"document"
para poder navegar a una pagina web se usa el metodo get(). El metodo devuelve el documento HTML al navegador para desplegarlo y mostrarlo.
"get("URL")"

"""
# get("URL") - metodo get()

# --- CODIGO DE EJEMPLO ---
# http request
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() 
# .encode() prepara los datos para q vayan por internet
# ^ lo convierte en UTF-8 bytes 
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='') 
    # usamos decode para poder procesar/ver la info q hemos codificado previamente
mysock.close()
"""
--- http header ---
HTTP/1.1 200 OK
Date: Tue, 21 Mar 2023 20:23:49 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
--- http body ---
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""

# --- ESCRIBIR UN NAVEGADOR ---
"""
^^^^^^
"""
# --- USANDO urllib  ---
# como el socket pero mas cortos
print("-------------------------------------------")
import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
"""
But soft what light through yonder window breaks
It is the east and Juliet is the sun    
Arise fair sun and kill the envious moon
Who is already sick and pale with grief 
"""
# lo podemos tratar como un fichero: 
print("-------------------------------------------")
# import urllib.request, urllib.parse, urllib.error
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# --- WEB SCRAPING --- 
# es la accion de recuperar una pagina web, extrayendo los links de esta, haciendo una cola de link no recuperados
# libreria: BeautifulSoup de crummy.com
"""
instalacion de la liberia:
https://pypi.python.org/pypi/beautifulsoup4 o https://www.py4e.com/code3/bs4.zip

-- CODIGO DE EJEMPLO ---
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup    # habria q instalar bs4
url = input("Enter -")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
# retrieve all of the anchor tags (<a href=.../>)
tags = soup('a')
for tag in tags:
    print(tag.get("href", None))
"""


