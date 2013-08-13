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

if __name__ == "__main__":
	#text = "{{SkyrimBooks |id = 000F6928}}"
	#f = open('test2_aeri','r')
	wikicode = parsePage("Bounty (Book)")
	#wikicode = mwph.parse(f.read())
	#print wikicode
	templates = wikicode.filter_templates()
	#print templates
	#print templates[0].get("id").value.strip()
	for i in templates:
		if i.name.strip() == "SkyrimBooks":
			print "ID:",i.get("id").value.strip()
