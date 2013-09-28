#!/usr/bin/env python

import json
import urllib
import mwparserfromhell as mwph

def parsePage(title):
	apiURL = "http://elderscrolls.wikia.com/api.php"
	data = {"action": "query", "prop":"revisions", "rvlimit":1, "rvprop":"content", "format":"json", "titles":title}
	raw = urllib.urlopen(apiURL, urllib.urlencode(data)).read()
	res = json.loads(raw)
	#print res
	text = res["query"]["pages"].values()[0]["revisions"][0]["*"]
	return mwph.parse(text)

def getID(title):
	#text = "{{SkyrimBooks |id = 000F6928}}"
	#f = open('test2_aeri','r')
	wikicode = parsePage(title)
	#wikicode = mwph.parse(f.read())
	#print wikicode
	templates = wikicode.filter_templates()
	#print templates
	#print templates[0].get("id").value.strip()
	for i in templates:
		if i.name.strip() == "SkyrimBooks":
			return i.get("id").value.strip()
	return "{{missing|Skyrim}}"

# in the event that there are linebreaks in the string; should probably be combined with "getID()"
def parseList(ids):
	import re
	total = re.split("<br[ /]*?>",ids)
	for i in xrange(len(total)): # get the strings out of unicode (is this a good idea?)
		total[i]=str(total[i]).strip()
	total=filter(None,total) # remove empty elements
	return total

if __name__ == "__main__":
	#print parseList(getID("Bounty (Book)"))
	import io,sys
	infile = open(sys.argv[1],'r')
	idhash={}
	for i in infile.readlines():
		ID=getID(i.strip())
		if ID:
			idhash[i]=parseList(ID)
			print i,parseList(ID)
	
