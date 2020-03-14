import urllib
import xml.etree.ElementTree as ET
import urllib.request

url = input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print("Retrieving " + url)

xml = urllib.request.urlopen(url)
s = xml.read()

print("Retrieved: " + str(len(s)) + " characters")

tree = ET.fromstring(s)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator += int(count.text)

print("Sum:" + str(accumulator))
