"""
Exercise  12.5: (Advanced) Change the socket program so that it only shows
data after the headers and a blank line have been received. Remember that
recv is receiving characters (newlines and all), not lines.

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Daniel Lee, Dec 29, 2019
"""
import socket

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4   # Finds the end of header
                                            # Adds four to exclude:'\r\n\r\n'
print(message[header_end_pos:],end='')
while True:                                 # Header in the first data only
    data = my_sock.recv(512)
    if len(data) <1 :
        break
    print(data.decode())
my_sock.close()
