promotors = [
    {'name': 'Jan', 'surname':'Kowalski', 'sell': 100, 'brand':'Sony'},
    {'name': 'Janusz', 'surname': 'Kowalczyk', 'sell': 200, 'brand':'Sony'},
    {'name': 'Janko', 'surname': 'Kowalewski', 'sell': 300, 'brand':'TCL' },
]

best = {p['name']: p['sell'] for p in promotors if p['sell'] >= 200}
print(f'Promotorzy, którzy sprzedali co najmniej 200 sztuk: {best}')