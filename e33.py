#!/usr/bin/python
import urllib2
import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'

url = "http://eda-libs.cisco.com/cadlibportal?ticket=ST-563-Rh6ePR0tum0OPLFubFJ2-pds-service.cisco.com"

user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Tr ident/5.0;'

headers = {'User-Agent':user_agent}
req = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(req)

the_page = response.read()

print(the_page)