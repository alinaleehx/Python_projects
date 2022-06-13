import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = 'http://py4e-data.dr-chuck.net/comments_1370137.json'
connection = urllib.request.urlopen(url, context=ctx)
data =connection.read().decode()

info = json.loads(data)

count = len(info['comments'])
sum = 0
for comment in info['comments']:
    num = comment['count']
    sum += num
print("count is {0}. Sum is {1}".format(count, sum))