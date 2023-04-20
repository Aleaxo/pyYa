import requests
import json

url = "https://api.weather.yandex.ru/v2/forecast?"
api_params={
	"lat":float,
	"lon":float,
	"lang":"ru_RU",
	"limit":1,
	"hours":"False",
	"extra":"True"
	}
head_params = {
'X-Yandex-API-Key':'your_key'
	}

s = requests.get(url,params=api_params,headers=head_params)

weather = s.json()


print("Temp     = "+str(weather["fact"]["temp"]))

