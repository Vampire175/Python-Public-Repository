import requests
import json
print('Welcome to Dictionary App')
word = input('Enter the word: ')
url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
r = requests.get(url)

if r.status_code == 200:  # Check if the request was successful
    wdict = json.loads(r.text)
    definitions = wdict[0]["meanings"][0]["definitions"]  # Accessing definitions
    print("Definitions:")
    for definition in definitions:
        print("-", definition["definition"])
else:
    print("Failed to fetch definition. Error:", r.status_code)
print('Thanks for using Dictionary App\nMade by Vampire with ❤️')
hd=input('Press Enter to exit')