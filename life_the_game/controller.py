def aktualizacja():
    global widok_siatki
    widok_siatki.delete(ALL)
    modul_zera.nastepne_pokolenie()

    for i in range(0, modul_zera.wys):
        for j in range(0, modul_zera.szer):
            if modul_zera.model_siatki[i][j] == 1:
                narysuj_komorke(i, j, 'black')

def narysuj_komorke(rzad, kolumna, kolor):
    global widok_siatki, wielkosc_komorki

    if kolor == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    widok_siatki.create_rectangle(rzad*wielkosc_komorki,
                                    kolumna*wielkosc_komorki,
                                    rzad*wielkosc_komorki+wielkosc_komorki,
                                    kolumna*wielkosc_komorki+wielkosc_komorki,
                                    fill=kolor, outline=outline)
