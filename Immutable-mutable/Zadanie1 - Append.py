# Kod + print(id(lista)) przed/po append
lista = [1, 2]
print("ID przed:", id(lista))
lista.append(3)
print("ID po:", id(lista))
print("Lista:", lista)
