# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
name = ""
url = "http://py4e-data.dr-chuck.net/known_by_Ellie.html"
# Retrieve all of the anchor tags
for x in range(7):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    pos = 1
    for tag in tags:
    # Look at the parts of a tag
        if (pos < 18):
            pos += 1
            continue
        url = str(tag.get('href', None))
        if (x == 6):
            name += tag.contents[0]
        break
print(name)