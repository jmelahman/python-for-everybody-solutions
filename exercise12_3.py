"""
Exercise  12.3: Use urllib to replicate the previous exercise of (1) retrieving
the document from a URL, (2) displaying up to 3000 characters, and (3) counting
the overall characters in the document. Don't worry about the headers for this
exercise, simply show the first 3000 characters of the document contents.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance
"""
import urllib.request


fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
chars = 0
char_limit = 3000
for line in fhand:
    # \n is considered a character; this follow commands like wc.
    # Change the following to line.decode().rstrip('\n') if desired
    line = line.decode()
    next_count = chars + len(line)
    if next_count <= char_limit:
        print(line.rstrip('\n'))
    elif chars < char_limit:
        char_remain = char_limit - chars - 1
        print(line[:char_remain])
    chars = next_count
print(chars)
