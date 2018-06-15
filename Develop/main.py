#coding=utf-8
import urllib.parse
import urllib.request
import json
import sys

if  len(sys.argv)== 1:
    location = input('what is your location?')
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
print(s["results"][0]["index"][0]["title"])
print(s["results"][0]["index"][0]["zs"])
print(s["results"][0]["index"][0]["tipt"])
print(s["results"][0]["index"][0]["des"])
print("\n")
print(s["results"][0]["index"][1]["title"])
print(s["results"][0]["index"][1]["zs"])
print(s["results"][0]["index"][1]["tipt"])
print(s["results"][0]["index"][1]["des"])
print("\n")
print(s["results"][0]["index"][2]["title"])
print(s["results"][0]["index"][2]["zs"])
print(s["results"][0]["index"][2]["tipt"])
print(s["results"][0]["index"][2]["des"])
print("\n")
print(s["results"][0]["index"][3]["title"])
print(s["results"][0]["index"][3]["zs"])
print(s["results"][0]["index"][3]["tipt"])
print(s["results"][0]["index"][3]["des"])
print("\n")
print(s["results"][0]["index"][4]["title"])
print(s["results"][0]["index"][4]["zs"])
print(s["results"][0]["index"][4]["tipt"])
print(s["results"][0]["index"][4]["des"])
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