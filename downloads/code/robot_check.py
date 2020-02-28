#!/usr/bin/python

import httplib
import urllib2

ip = '10.10.10.141'
img_name = 'cat_the_troll.jpg'

# read URIs found in robots.txt
f = open('robots.txt','r')
uri_list = f.readlines()
f.close()

uri_to_check = []

print '[*] Start checking ...'
for uri in uri_list:
	conn = httplib.HTTPConnection(ip)
	conn.request('GET', (uri.rstrip('\n')+'/'))
	response = conn.getresponse()

	if response.status != 404:							# filter error code 404 to make the result nice and tidy
		print '[+] ' + uri.rstrip('\n')+'/'
		print '[-] ' + str(response.status)
		uri_to_check.append('http://' + ip + uri.rstrip('\n') + '/' + img_name)	# if the response code is not 404 then put in uri_to_check list for further analysis

# save under inspection URIs to file for further analysis
print '[*] Saving result to file: uris_to_check.txt'
f = open('uris_to_check.txt', 'w')
for uri in uri_to_check:
	f.write(uri + '\n')
f.close()

print '[*] Done!'