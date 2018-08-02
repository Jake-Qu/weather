#coding=utf-8
import urllib.parse
import urllib.request
import json
import sys

##获取IP地址并且获得地理位置
def get_locatoin():
    urls = 'http://members.3322.org/dyndns/getip'
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        ip = response.read().decode('utf-8')
    urls = 'http://freeapi.ipip.net/' + ip
    req = urllib.request.Request(urls)
    with urllib.request.urlopen(req) as response:
        local = response.read()
        c = local.decode('utf-8')
        return c.split('''"''')[5]

#获取地理位置的两种方式
if  len(sys.argv)== 1:
    location = input('what is your location?')
    if location == "":
        location = get_locatoin()
else:
    location = sys.argv[1]




#取得天气
def get_weather(location):

    r_location = urllib.parse.quote(location)
    link = 'http://api.map.baidu.com/telematics/v3/weather?location=' + r_location +'&output=json&ak=KPGX6sBfBZvz8NlDN5mXDNBF&callback='
    req = urllib.request.Request(link)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    s = json.loads(the_page)
    print("您的地点是：",location +".\n"+ "今日各项指数：")

    for i in range(1,5):
        for k in ['title','zs','tipt','des']:
            try:
                print(s["results"][0]["index"][i][k])
            except KeyError:
                print("Sorry, we can't currently check the weather outside of China.")
                exit(1)
        print("\n")

    print (s["results"][0]["currentCity"])
    for b in range(0,4):
        print (s["results"][0]["weather_data"][b]["date"]+ '天气:')
        for k in ['weather','wind','temperature']:
            print (s["results"][0]["weather_data"][b][k])
        print("\n")

#赋值传参
get_weather(location)