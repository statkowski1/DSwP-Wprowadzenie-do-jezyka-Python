#Zadanie 1

data = input('Podaj dane rozdzielone dowolnym separatorem: ')
source_separator = input('Podaj separator źródłowy: ')
target_separator = input('Podaj separator docelowy: ')

splited_data = data.split(source_separator)
joined_data = target_separator.join(splited_data)

print('Dane z zmodyfikowanym separatorem: ', joined_data)

#Zadanie 2

data2 = input('Podaj łańcuch znaków: ')

middle_index_data2 = len(data2) // 2
first_part = data2[:middle_index_data2]
second_part = data2[middle_index_data2:]

print('Pierwsza część łańcucha znaków: ', first_part)
print('Druga część łańcucha znaków: ', second_part)

print('Łańcuch znaków wyświetlony co drugi znak od końca: ', data2[::-2])

#Zadanie 3

data3 = 'deus ex machina'

print(data3)
print('title(): ', data3.title())
print('capitalize(): ', data3.capitalize())
print('zfill(20): ', data3.zfill(20))
print('upper(): ', data3.upper())
print('count(): ', data3.count('e'))
print('center(20, \'*\'): ', data3.center(20, '*'))

#Zadanie 4

data4 = input('Podaj dowolny łańcuch znaków: ')

print('isalpha(): ', data4.isalpha())
print('isascii(): ', data4.isascii())
print('isprintable(): ', data4.isprintable)
print('istitle(): ', data4.istitle())
print('isupper(): ', data4.isupper())

#Zadanie 5

data5_1 = '{:>15}'.format('cortex')
print(data5_1)

data5_2 = '{}! * {}!'.format(3, 7)
print(data5_2)

data5_3 = '{:_<15}'.format('cerebrum')
print(data5_3)

data5_4 = '{:07.3f}'.format(1.618033988749894)
print(data5_4)

data5_5 = '{:=+10d}'.format(1024)
print(data5_5)

#Zadanie 6

data6 = ['\u2765', '\u0906', '\u16EF', '\u2103', '\u216B', '\u2211', '\u23F3', '\u2744', '\u2F4B', '\uAB62']

for x in data6:
    print(f'Znak: {x}, int reprezentujący unicode: {ord(x)}, znak po użyciu int reprezentującego unicode tego znaku: {chr(ord(x))}')

