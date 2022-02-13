for i in range(0, 1000):
    nazwa_pliku = lancuch(i) + '.txt'
    plik = open(nazwa_pliku, 'r')
    tekst = plik.read()
    if 'igła' in tekst:
        print('Znalazłem igłę w stosie plików.' + lancuch(i) + '.txt')
        break
    plik.close()
    break
print('Zakończono wyszkukiwanie')
