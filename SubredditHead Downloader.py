# SubReddit ImageDownloader.py
# Download the reddit alien image to a local folder.

import urllib
import urllib2
import re

url = raw_input("Please enter a SubReddit URL: ")
urlContent = urllib2.urlopen(url).read()
# Finds all the image urls 
imgurls = re.findall('img .*?src="(.*?)"', urlContent)

print "The source code of the image is " + imgUrls[0]

local = raw_input(
    "Please indicate the folder that you want to save the Reddit picture(e.g. d:\new): ")+ "//reddit.jpg"

urllib.urlretrieve(imgurls[0], local)

