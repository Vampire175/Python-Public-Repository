import requests
import json
import webbrowser
print('Welcome to Weather App by Vampire')
webbrowser.open('https://www.weatherapi.com/')
a=input('Enter City Name: ')
b=input('Enter your api key: ')
c=input('Enter the Country name: ')
url=f'https://api.weatherapi.com/v1/current.json?key={b}&q={a,c}'
r=requests.get(url)
#print(r.text)
wdict=json.loads(r.text)
print(wdict["current"]["temp_c"])
print('Thanks for using Weather App by Vampire')
print('Made by Vampire with ❤️')
gh=input('Press Enter to exit')