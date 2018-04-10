#coding=utf-8
import urllib.parse
import urllib.request
import json
import sys

#获取地理位置的两种方式
if  len(sys.argv)== 1:
    location = input('what is your location?')
    if location == "":
        location = '北京'
else:
    location = sys.argv[1]

##获取IP地址并且获得地理位置
def get_locatoin():
    urls = 'http://members.3322.org/dyndns/getip'
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        ip = response.read()
        #print(ip.decode('utf-8'))
        r_ip = ip.decode('utf-8')
        return r_ip
    urls = 'http://freeapi.ipip.net/' + r_ip
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        local = response.read()
        print(local.decode('utf-8'))

#取得天气
def get_weather(locations):
    r_location = urllib.parse.quote(locations)
    link = 'http://api.map.baidu.com/telematics/v3/weather?location=' + r_location +'&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback='
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    #print (the_page)
    s = json.loads(the_page);
    print("今日各项指数：")
    for i in range(1,5):
        print(s["results"][0]["index"][i]["title"])
        print(s["results"][0]["index"][i]["zs"])
        print(s["results"][0]["index"][i]["tipt"])
        print(s["results"][0]["index"][i]["des"])
        print("\n")

    for b in range(0,4):
        print (s["results"][0]["currentCity"])
        print (s["results"][0]["weather_data"][b]["date"]+ '天气')
        print (s["results"][0]["weather_data"][b]["weather"])
        print (s["results"][0]["weather_data"][b]["wind"])
        print (s["results"][0]["weather_data"][b]["temperature"])
        print("\n")
#赋值传参
locations = location
get_weather(locations)
