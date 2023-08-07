import random

def hangman():
    words = ['Apfel', 'Banane', 'Orange', 'Erdbeere', 'Ananas']
    word = random.choice(words).lower()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('Du hast noch', lives, 'Leben übrig und hast diese Buchstaben benutzt: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Aktuelles Wort: ', ' '.join(word_list))

        user_letter = input('Rate einen Buchstaben: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Buchstabe ist nicht im Wort.')
        elif user_letter in used_letters:
            print('Du hast diesen Buchstaben bereits benutzt. Versuche es erneut.')
        else:
            print('Ungültiger Buchstabe. Versuche es erneut.')

    if lives == 0:
        print('Du hast verloren, das Wort war', word)
    else:
        print('Herzlichen Glückwunsch, du hast gewonnen!')

hangman()

import requests

def get_gas_prices(postal_code):
    url = 'https://api.example.com/gasprices'
    params = {'postal_code': postal_code}
    response = requests.get(url, params=params)
    data = response.json()
    return data['prices']

postal_code = '12345'
prices = get_gas_prices(postal_code)
print('Aktuelle Tankpreise für Postleitzahl {}:'.format(postal_code))
for price in prices:
    print('{}: {:.2f} €/L'.format(price['type'], price['price']))

