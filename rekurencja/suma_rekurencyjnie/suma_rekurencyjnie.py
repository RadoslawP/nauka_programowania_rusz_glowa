kulki = [10, 13, 39, 14, 41, 9, 3]

def oblicz_sume_rekurencyjnie(lista):
    if len(lista) == 0:
        return 0
    else:
        pierwszy = lista[0]
        reszta = lista[1:]
        suma = pierwszy + oblicz_sume_rekurencyjnie(reszta)
        return suma

suma = oblicz_sume_rekurencyjnie(kulki)
print('Kulek jest łącznie', suma)
