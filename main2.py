#coding=utf-8
import urllib.parse
import urllib.request
import json
import sys

if  len(sys.argv)== 1:
    location = input('what is your location?')
    if location == "":
        location = '北京'
else:
    location = sys.argv[1]
r_location = urllib.parse.quote(location)
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
print("今天天气：")
print (s["results"][0]["currentCity"])
print (s["results"][0]["weather_data"][0]["date"])
print (s["results"][0]["weather_data"][0]["weather"])
print (s["results"][0]["weather_data"][0]["wind"])
print (s["results"][0]["weather_data"][0]["temperature"])
print("\n")

print("明天天气：")
print (s["results"][0]["weather_data"][1]["date"])
print (s["results"][0]["weather_data"][1]["weather"])
print (s["results"][0]["weather_data"][1]["wind"])
print (s["results"][0]["weather_data"][1]["temperature"])