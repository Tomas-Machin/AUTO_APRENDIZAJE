import xml.etree.ElementTree as ET
import json

data = '''<person>
    <name> Chuck </name>
    <phone> type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
    </person>'''

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Attr:", tree.find("email").get("hide"))

# Name:  Chuck 
# Attr: yes

print("-----------------------------------------")
input = '''<stuff>
    <users>
        <user x="2">
            <id> 001 </id>
            <name> Chuck </name>
        </user>
        <user x="7">
            <id> 009 </id>
            <name> Brent </name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall("users/user")
print("User count:", len(lst))
for item in lst:
    print("Name:", item.find("name").text)
    print("Id:", item.find("id").text)
    print("Attribute", item.get("x"))

# User count: 2
# Name:  Chuck
# Id:  001
# Attribute 2
# Name:  Brent
# Id:  009
# Attribute 7import json

data = '''{
    "name":"Chuck",
    "phone":{
        "type":"intl",
        "number":"+1 734 303 4456"
    },
    "email": {
        "hide":"yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])

# Name: Chuck
# Hide: yes  