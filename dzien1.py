# List comprehension - mutable vs immutable
dane = [1, 2, 3, 4, 5]
kwadraty = [x**2 for x in dane if x % 2 == 0]
print(kwadraty)  # [4, 16]

# Dict mutable
slownik = {'promotor': 'sales', 'raport': 'pandas'}
slownik['nowy'] = 'venv'
print(slownik)
