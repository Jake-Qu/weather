import urllib.parse
import urllib.request
import json
import sys


def get_locatoin():
    urls = 'http://members.3322.org/dyndns/getip'
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        ip = response.read()
        #print(ip.decode('utf-8'))
        r_ip = ip.decode('utf-8')
    urls = 'http://freeapi.ipip.net/' + r_ip
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        local = response.read()
        c = local.decode('utf-8')
        return c

result = get_locatoin()
list = result.split('''"''')
print(list[5])


