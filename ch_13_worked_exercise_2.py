# Chapter 13 ex 2. Write a program that will prompt to enter in a url, read the JSOPN data from that URL using
# urllib and then parse and extract the comment counts from the JSON data,
# compute the sum of the numbers in the file and enter the sum below


import json
import urllib.request
import urllib.error
import urllib.parse
import ssl

site = input('Enter URL: ')
# 'http://py4e-data.dr-chuck.net/comments_42.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_list = urllib.request.urlopen(site, context=ctx).read()

json_list = json.loads(file_list)

json_clean = json_list['comments']

total = 0

for i in json_clean:
    x = i['count']
    total = x + total

print(total)
