import time # moduł time do obliczenia czasu procesu

# liczenie ciągu fibonacci metodą rekurencyjną
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# kod testowy
for i in range(20, 55, 5):
    początek = time.time()
    wynik = fibonacci(i)
    koniec = time.time()
    czas = koniec - początek
    print(i, wynik, czas)
