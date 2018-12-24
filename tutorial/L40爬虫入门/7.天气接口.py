# 免费的天气接口https://www.sojson.com/blog/305.html
import  urllib.request
import json
url='http://t.weather.sojson.com/api/weather/city/101180101'
resp=urllib.request.urlopen(url)
if resp.code==200:
    weather_json=resp.read().decode('utf-8')
    print(type(weather_json),weather_json)
    weather_data =json.loads(weather_json)
    data=weather_data['data']
    print('\n\n',data)

    today_humidity = data['shidu']
    today_pm25=data['pm25']
    today_temperature=data['wendu']
    today_ganmao=data['ganmao']
    print(f'今天的湿度是{today_humidity}，pm25是{today_pm25},湿度是{today_temperature}，今天的天气状况：{today_ganmao}')


