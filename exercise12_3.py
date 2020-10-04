"""
Exercise  12.3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall characters in the document. Don't worry about the headers for this
exercise, simply show the first 3000 characters of the document contents.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Daniel Lee, Dec 29, 2019
"""
import urllib.request
url = input('Enter URL: ')
fhand = urllib.request.urlopen(url)
count = 0
for line in fhand:
    sline = line.decode().strip()
    if count + len(sline) <= 3000:
        print(sline)
    elif count < 3000 and count + len(sline) > 3000:
        numchar = 3000 - count
        print(sline[:numchar - 1])
    count += len(sline)
print(count)
