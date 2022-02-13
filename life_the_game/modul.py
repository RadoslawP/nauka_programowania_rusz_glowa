wys = 100
szer = 100

model_siatki = [0] * wys
nastepny_model_siatki = [0] * wys
for i in range(wys):
    model_siatki[i] = [0] * szer
    nastepny_model_siatki[i] = [0] * szer

def nastepne_pokolenie():
    global model_siatki, nastepny_model_siatki

    for i in range(0, wys):
        for j in range(0, szer):
            komorka = 0
            #print('Sprawdzam komórkę', i, j)
            licznik = policz_sasiadow(model_siatki, i, j)

            if model_siatki[i][j] == 0:
                if licznik == 3:
                    komorka = 1
            elif model_siatki[i][j] == 1:
                if licznik == 2 or licznik == 3:
                    komorka = 1
            nastepny_model_siatki[i][j] = komorka

tymczasowa = model_siatki
model_siatki = nastepny_model_siatki
nastepny_model_siatki = tymczasowa

def policz_sasiadow(siatka, szer, wys):
    licznik = 0

    if rzad-1 >= 0:
        licznik = licznik + siatka[rzad-1][kolumna]
    if (rzad-1 >= 0) and (kolumna-1 >= 0):
        licznik = licznik + siatka[rzad-1][kolumna-1]
    if (rzad-1 >= 0) and (kolumna+1 < szer):
        licznik = licznik + siatka[rzad-1][kolumna+1]
    if kolumna-1 >= 0:
        licznik = licznik + siatka[rzad][kolumna-1]
    if kolumna+1 < szer:
        licznik = licznik + siatka[rzad][kolumna+1]
    if rzad+1 < wys:
        licznik = licznik + siatka[rzad+1][kolumna]
    if (rzad+1 < wys) and (kolumna-1 >= 0):
        licznik = licznik + siatka[rzad+1][kolumna-1]
    if (rzad+1 < wys) and (kolumna+1 < szer):
        licznik = licznik + siatka[rzad+1][kolumna+1]

    return licznik


if __name__ == '__main__':
    nastepne_pokolenie()
