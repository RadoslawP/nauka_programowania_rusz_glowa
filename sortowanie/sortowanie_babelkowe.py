def sortowanie_babelkowe(wyniki, numery):
    zamiana = True
    while zamiana:
        zamiana = False
        for i in range(0, len(wyniki)-1):
            if wyniki[i] < wyniki[i+1]:
                tymczasowa = wyniki[i]
                wyniki[i] = wyniki[i+1]
                wyniki[i+1] = tymczasowa
                tymczasowa = numery[i]
                numery[i] = numery[i+1]
                numery[i+1] = tymczasowa
                zamiana = True

wyniki = [60, 50, 60, 58, 54, 54,
          58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51,
          69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18,
          41, 53, 55, 61, 51, 44]

liczba_wynikow = len(wyniki)
numery_roztworow = list(range(liczba_wynikow))

sortowanie_babelkowe(wyniki, numery_roztworow)

print("Najlepsze roztwory na banki:")
for i in range(0,5):
    print(str(i+1) + ')',
    "Wyniki roztworu #" + str(numery_roztworow[i]),
    "to:", wyniki[i])
