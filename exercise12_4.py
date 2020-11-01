#!/usr/bin/env python3
"""
Exercise  12.4: Change the urllinks.py program to extract and count paragraph
(p) tags from the retrieved HTML document and display the count of the
paragraphs as the output of your program. Do not display the paragraph text,
only count them. Test your program on several small pages as well as some
larger web pages.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


count = 0                               # Initialize variables
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    count += 1                          # Counter
print(count)
