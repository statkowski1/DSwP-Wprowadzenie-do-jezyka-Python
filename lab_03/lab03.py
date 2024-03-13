#Zadanie 1

list1 = [x for x in range(1, 11)]
print('Początkowa lista: ', list1)

list2 = list1[5:]
list1 = list1[:5]
print('Pierwsza lista po podziale: ', list1)
print('Druga lista po podziale: ', list2)

#Zadanie 2

list3 = list1 + list2
print('Połączone listy: ', list3)

list3.insert(0, 0)
print('Dodanie liczby na początku listy: ', list3)

list4 = sorted(list3, reverse=True)
print('Posortowana lista malejąco: ', list4)

#Zadanie 3

text = input('Wprowadź dowolny tekst: ')
unique_text_chars = sorted(set(text.lower()))
print('Unikalne znaki w tekście posortowane alfabetycznie: ', unique_text_chars)

#Zadanie 4

dictionary1 = {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec', 7: 'Lipiec', 8: 'Sierpień',
               9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'}
print('Słownik z polskimi nazwami miesięcy: ', dictionary1)

#Zadanie 5

dictionary2 = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
               9: 'September', 10: 'October', 11: 'November', 12: 'December'}
print('Słownik z angielskimi nazwami miesięcy: ', dictionary2)

dictionary3 = {'pl': dictionary1, 'en': dictionary2}
print('\nPołączone słowniki z miesiącami (polski i angielski): ', dictionary3)

print('\nPrzykłady:')
print(dictionary3['pl'][4])
print(dictionary3['en'][4])

#Zadanie 6

text2 = 'Marianna'
unique_text2_chars = dict.fromkeys(text2, 1)
print(unique_text2_chars)

#Zadanie 7

import string

text3 = input('Podaj dowolny łańcuch znaków: ')

lowercase_count = sum(1 for char in text3 if char.lower() in string.ascii_lowercase)
digits_count = sum(1 for char in text3 if char.isdigit())

lowercase_percent = (lowercase_count / len(text3)) * 100
digits_percent = (digits_count / len(text3)) * 100

print('Liczba znaków w podanym łańcuchu znaków: ', len(text3))
print(f'Udział procentowy liter w podanym łańcuchu znaków: {lowercase_percent: .2f}%')
print(f'Udział procentowy cyfr w podanym łańcuchu znaków: {digits_percent: .2f}%')
