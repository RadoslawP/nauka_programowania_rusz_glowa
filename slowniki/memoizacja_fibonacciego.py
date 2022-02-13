import time

bufor = {}

def fibonacci(n):
    global bufor
    if n in bufor:
        return bufor[n]

    if n == 0:
        wynik = 0
    elif n == 1:
        wynik = 1
    else:
        wynik = fibonacci(n-1) + fibonacci(n-2)
    bufor[n] = wynik
    return wynik

poczatek = time.time()

for i in range(0, 101):
    wynik = fibonacci(i)
    print(i, wynik)

koniec = time.time()
czas = koniec - poczatek
print('Wszystkie 100 liczb obliczono w', czas, 'sekund.')
