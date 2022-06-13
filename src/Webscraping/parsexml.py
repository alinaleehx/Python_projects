import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1370136.xml'
connection = urllib.request.urlopen(url, context=ctx)

data = connection.read().decode()
print('Retrieved', len(data), 'characters')
sum = 0
tree = ET.fromstring(data)
comments = tree.find('comments')
for comment in comments:
    num = comment.find('count').text
    sum += int(num)

print("Sum is {0}".format(sum))
