#!/usr/bin/python

import socket
import re

ip = "127.0.0.1"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn = s.connect((ip,port))
res = s.recv(1024)
print res
s.send('START/n')
res = s.recv(1024)
print res

while True:
	res = s.recv(1024)
	data = re.findall(r"Quick what's\.\.\. (.*)\?", res)
	if not data:
		print "pattern is not found!"
		print res
		break
	else:
		(a,b) = data[0].split(' x ')
		rst = int(a) * int(b)
		print rst
		s.send(str(rst)+'\n')

print '[*] Done!'
s.close()
