import requests
import json
import webbrowser
print('Welcome to Indian News App by Vampire')
webbrowser.open('https://newsapi.org/')
p=input('What is your api key- ')
url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={p}'
r = requests.get(url)
wdict = json.loads(r.text)

# Check if the request was successful
if wdict['status'] == 'ok':
    # Extract articles
    articles = wdict['articles']
    
    # Extract article names
    article_names = [article['title'] for article in articles]
    
    # Print article names with lines
    for name in article_names:
        print(name)
        print('-' * len(name))  # Line separator with the same length as the article name
else:
    print("Failed to fetch news:", wdict['message'])
print('Thanks for using Indian News App by Vampire')
print('Made by Vampire with ❤️')
gh=input('Press Enter to exit')