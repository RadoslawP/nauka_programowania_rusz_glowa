try:
    liczba = input('Podaj liczbę: ')
    wynik =42 / int(liczba)
except ZeroDivisionError:
    print("Nie dzieli się przez zero!")
except ValueError:
    print("Miałeś podać liczbę.")
else:
    print('Twój wynik to', wynik)
finally:
    print('Dzięki za wypróbowanie progranmu.')
