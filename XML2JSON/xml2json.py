import json2xml
import xmltodict
import os
import json
from xml.etree import ElementTree as ET

def dumptofile(roomjson):
    with open("tempjson.txt", "w", encoding="utf-8") as f:
        json.dump(roomjson, f, ensure_ascii=False, indent=0)

def loadfromxml(xmlfilename):
    xmlf = open(xmlfilename,"r")
    roomjson = xmltodict.parse(xmlf.read())
    xmlf.close()
    return roomjson