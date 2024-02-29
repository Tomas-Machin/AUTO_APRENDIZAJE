<<<<<<< HEAD
# --- JSON, XML ---
# XSD: W3C Schema specification de XML
"""
estructura XSD:
- xs:complexType 
- xs:sequence
- xs:element
--- EJEMPLO ---
<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>
--- EQUIVALENTE EN XML ---
<person>
 <lastname> Severance </lastname>
 <age> 17 </age>
 <dateborn> 2001-04-17 </dateborn>
</person>
------------------------------
        CONSTRAINTS
------------------------------
<xs:element name="person">
 <xs:complexType>
  <xs:sequence>
   <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1"/>
   <xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10"/>
  </xs:sequence>
 </xs:complexType>
</xs:element>
--- EQUIVALENTE EN XML ---
<person>
 <full_name> Tove Refsnes </full_name>
 <child_name> Hege </child_name>
 <child_name> Stale </child_name>
 <child_name> Jim </child_name>
 <child_name> Borge </child_name>
</person>
------------------------------
      tipos de datos XSD
------------------------------
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>
--- EQUIVALENTE EN XML ---
<customer> John Smith </customer>
<start> 2002-09-24 </start>
<startdate> 2002-05-30T9:30:10Z </stardate>  # date, time of the day, timezone
<prize> 999.50 </prize>
<weeks> 30 </weeks>
"""

import xml.etree.ElementTree as ET

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
# Attribute 7

print("-----------------------------------------")
# ---- JSON ----
# codigo de ejemplo:
import json
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
=======
# --- JSON, XML ---
# XSD: W3C Schema specification de XML
"""
estructura XSD:
- xs:complexType 
- xs:sequence
- xs:element
--- EJEMPLO ---
<xs:complexType name="person">
 <xs:sequence>
  <xs:element name="lastname" type="xs:string"/>
  <xs:element name="age" type="xs:integer"/>
  <xs:element name="dateborn" type="xs:date"/>
 </xs:sequence>
</xs:complexType>
--- EQUIVALENTE EN XML ---
<person>
 <lastname> Severance </lastname>
 <age> 17 </age>
 <dateborn> 2001-04-17 </dateborn>
</person>
------------------------------
        CONSTRAINTS
------------------------------
<xs:element name="person">
 <xs:complexType>
  <xs:sequence>
   <xs:element name="full_name" type="xs:string" minOccurs="1" maxOccurs="1"/>
   <xs:element name="child_name" type="xs:string" minOccurs="0" maxOccurs="10"/>
  </xs:sequence>
 </xs:complexType>
</xs:element>
--- EQUIVALENTE EN XML ---
<person>
 <full_name> Tove Refsnes </full_name>
 <child_name> Hege </child_name>
 <child_name> Stale </child_name>
 <child_name> Jim </child_name>
 <child_name> Borge </child_name>
</person>
------------------------------
      tipos de datos XSD
------------------------------
<xs:element name="customer" type="xs:string"/>
<xs:element name="start" type="xs:date"/>
<xs:element name="startdate" type="xs:dateTime"/>
<xs:element name="prize" type="xs:decimal"/>
<xs:element name="weeks" type="xs:integer"/>
--- EQUIVALENTE EN XML ---
<customer> John Smith </customer>
<start> 2002-09-24 </start>
<startdate> 2002-05-30T9:30:10Z </stardate>  # date, time of the day, timezone
<prize> 999.50 </prize>
<weeks> 30 </weeks>
"""

import xml.etree.ElementTree as ET

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
# Attribute 7

print("-----------------------------------------")
# ---- JSON ----
# codigo de ejemplo:
import json
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
>>>>>>> 70eeabf7fe0392c3aa721948c166730523aa1e3e
# Hide: yes  