#immutable - Wartość nie da się zmienić w miejscu – nowa zmienna tworzy nowy obiekt w pamięci. inne id
x = 5
print(id(x))
x = 6
print(id(x))

#Mutable (zmienne): Zmiana modyfikuje oryginalny obiekt, bez zmianny id
lista = [1, 2, 3, 4, 5]
print(id(lista))
lista.append(6)
print(id(lista))