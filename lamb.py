"""
Wyrażenia lambda w Pythonie to anonimowe funkcje jednolinijkowe. 
Są bardzo użyteczne w określonych przypadkach, takich jak krótkotrwałe 
operacje na danych czy przekazywanie małych funkcji jako argumentów do innych funkcji.
"""

# przekształć podaną listę w listę zawierającą długości poszczególnych słów. 
stocks = ['playway', 'boombit', 'cd projekt']

len_stocks = list(map(lambda x: len(x), stocks))

print(len_stocks)

print('---')

# funkcja która uporządkuje listę składającą się z dwuelementowych 
# krotek - obiektów typu tuple według drugiego elementu krotki.

tuple_check_first = [(1, 3), (4, 1), (4, 2), (0, 7)]
tuple_check_second = [('a', 'b'), ('g', 'a'), ('z', 'd')]

def sort_list(tuple_check):
    return sorted(tuple_check, key=lambda x: x[1], reverse=False)

print(sort_list(tuple_check_first))
print(sort_list(tuple_check_second))

print('---')

# Ćwiczenie ma na celu pokazanie, że możliwe jest utworzenie funkcji nazwanej przy użyciu wyrażenia lambda.
def func_1 (x, y):
    return x + y + 2

print(func_1(4, 4))

def func_2(x, y):
    final = lambda x, y: x + y + 2
    return final(x, y)

print(func_2(4, 4))

print('---')

# Posortuj listę według rosnącej sumy kwadratów liczb podanych w obiektach typu tuple
items = [(3, 4), (2, 5), (1, 4), (6, 1)]

items.sort(key=lambda x: (x[0] + x[1])**2)

print(items)

print('---')

# Posortuj podaną listę słowników po kluczu price:
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

stocks.sort(key=lambda x: x['price'])

print(stocks)

print('---')

# wyodrębnij spółki z indeksu 'mWIG40' w postaci listy i wynik wydrukuj do konsoli. 
stocksTwo = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print((list(filter(lambda x: x['indeks'] == 'mWIG40', stocksTwo))))

print('---')

# Przekształć podaną listę na listę wartości logicznych (True, False). 
#True w przypadku, gdy spółka należy do indeksu 'mWIG40', False przeciwnie
stocksThree = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]
# I sposób:
trueOrFalse = [True if name['indeks'] == 'mWIG40' else False for name in stocksThree]
# II sposób:
trueOrFalseLambda = list(map(lambda x: True if x['indeks'] == 'mWIG40' else False, stocksThree))

print(trueOrFalse)
print(trueOrFalseLambda)

print('---')

# przekształć podaną listę w taki sposób, aby pozbyć się z każdego elementu znaku '-' (myślnik).
items = ['P-1', 'R-2', 'D-4', 'F-6']

itemsWithoutSign = list(map(lambda x: x.replace('-', ""), items))

print(itemsWithoutSign)

# przekształć podane listy w jedną zawierającą resztę z dzielenia elementu pierwszej listy przez odpowiedni element drugiej listy
num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]

num_1Andnum_2 = list(map(lambda x, y: x % y, num1, num2))

print(num_1Andnum_2)

