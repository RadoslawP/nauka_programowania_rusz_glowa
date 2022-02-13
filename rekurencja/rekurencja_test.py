kulki = [10, 13, 39, 14, 41, 9, 3]
def oblicz_sume(lista):
    suma = 0
    for liczba in lista:
        suma = suma + liczba
    return suma
print('Kulek jest łącznie', oblicz_sume(kulki))
