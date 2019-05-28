"""
Exercise  12.5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember that
recv is receiving characters (newlines and all), not lines.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 5, 2017
"""
import socket
import re

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
my_sock.send(cmd)

data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # Finds the end of header
                                            # Adds four to exclude:'\r\n\r\n'
print(message[header_end_pos:])
while True:                                 # Header in the first data only
    data = my_sock.recv(512)
    if not data:
        break
    print(data.decode())
my_sock.close()
