from json2xml import json2xml
import xmltodict
import dicttoxml
import os
import json
import sys
from xml.etree import ElementTree as ET
import xml2json as xml2json



   
rootdir = os.path.dirname(__file__)
sysarg = sys.argv[0]


filename = os.path.join(rootdir,"tempjson.txt")
print(filename)
data = "null"


try:
    file = open(filename,"r")
    data = file.read()
    data = data.replace("\\","")
    file.close()
except:
    print("temp file unfound")
    data = filename

"""
try:
    os.remove(os.path.join(rootdir,"tempjson.txt"))
except:
    print(os.path.join(rootdir,"tempjson.txt"))


"""


#load json and convert to xml
my_item_func = lambda x: 'list item'
outxml = dicttoxml.dicttoxml(json.loads(data), item_func=my_item_func,attr_type=False)

file = open(os.path.join(rootdir,"exportroom.xml"),"w")
file.write(str(outxml).replace("@",""))
file.close()
