import requests
from bs4 import BeautifulSoup
a=input('Enter the url: ')
response=url=a
u=requests.get(url)
soup=BeautifulSoup(u.text,'html.parser')
b=input('Which attribute do you want to get: ')
for all in soup.find_all(b):
    print(all.text)
print("Made by Vampire with ❤️")
c=input("Press Enter to exit")