import json2xml
import xmltodict
import os
import json
import sys
from xml.etree import ElementTree as ET
import xml2json as xml2json

def dumptofile(roomjson):
    print("Trying to dump to file")
    try:
        with open("tempjson.txt", "w", encoding="utf-8") as f:
            json.dump(roomjson, f, ensure_ascii=False, indent=0)
            print("success.")
    except:
        print("Unable to create file")
        

def loadfromxml(xmlfilename):
    xmlf = open(xmlfilename,"r")
    roomjson = xmltodict.parse(xmlf.read())
    xmlf.close()
    return roomjson

rootdir = os.path.dirname(__file__)

sysarg = sys.argv[0]

xmlfilename = os.path.join(rootdir,"rm_main.xml")

roomjson = xml2json.loadfromxml(xmlfilename)

xml2json.dumptofile(roomjson)

print(sysarg)








