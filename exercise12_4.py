"""
Exercise  12.4: Change the urllinks.py program to extract and count paragraph
(p) tags from the retrieved HTML document and display the count of the 
paragraphs as the output of your program. Do not display the paragraph text,
only count them. Test you program on several small pages as well as some larger
web pages.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 4, 2017
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0                               #Initializes variable
# Retrieve all of the anchor tags
tags = soup('p')
for tag in tags:
    count += 1                          #counter
print(count)