"""
Exercise  12.3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall characters in the document. Don't worry about the headers for this
exercise, simply show the first 3000 characters of the document contents.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 4, 2017
"""
import urllib.request
import urllib.parse
import urllib.error


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

characters = 0
for line in fhand:
    # \n is considered a character
    # Amend to line.decode().rstrip() if needed
    words = line.decode()
    characters = characters + len(words)
    if characters < 3000:
        print(line.decode().strip())
print(characters)
