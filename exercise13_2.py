#!/usr/bin/env python3
"""
Exercise 13.2: Write a program that will prompt to enter in a url, read the JSON data from that URL using
urllib and then parse and extract the comment counts from the JSON data,
compute the sum of the numbers in the file and enter the sum below.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
import json
import ssl
import urllib.request
import urllib.error
import urllib.parse


site = input('Enter URL: ')
# Short circuit to default URL if none is entered
site = site or 'http://py4e-data.dr-chuck.net/comments_42.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

file_list = urllib.request.urlopen(site, context=ctx).read()

json_list = json.loads(file_list)

comments = json_list['comments']

total = 0
for comment in comments:
    total += comment['count']

print(total)
