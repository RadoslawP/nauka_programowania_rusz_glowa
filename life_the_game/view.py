from tkinter import *
import modul_zera

wielkosc_komorki = 5
uruchomiony = False

def ustawienia():
    global okno_glowne, widok_siatki, wielkosc_komorki, przycisk_start, przycisk_wyczysc, wybor

    okno_glowne = Tk()
    okno_glowne.title('Life the game')

    widok_siatki = Canvas(okno_glowne, width = modul_zera.szer*wielkosc_komorki,
                                        height=modul_zera.wys*wielkosc_komorki,
                                        borderwidth=0,
                                        highlightthickness=0,
                                        bg='white')

    przycisk_start = Button(okno_glowne, text = 'Start', width = 12)
    przycisk_start.bind('<Button-1>', handler_start)
    przycisk_wyczysc = Button(okno_glowne, text = 'Wyczyść', width = 12)
    przycisk_wyczysc.bind('<Button-1>', handler_wyczysc)

    wybor = StringVar(okno_glowne)
    wybor.set('Wybierz wzorzec')
    opcja = OptionMenu(okno_glowne, wybor, 'Wybierz wzorzec',
                                            'szybowiec',
                                            'działo/szybowiec',
                                            'losowy',
                                            command=handler_opcji)
    opcja.config(width=20)

    widok_siatki.grid(row=0, columnspan=3, padx=20, pady=20)
    widok_siatki.bind('<Button-1>', handler_siatki)
    przycisk_start.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    opcja.grid(row=1, column=1, padx=20)
    przycisk_wyczysc.grid(row=1, column=2, sticky=E, padx=20, pady=20)

def handler_opcji(zdarzenie):
    global uruchomiony, przycisk_start, wybor

    uruchomiony = False
    przycisk_start.configure(text='Start')

    wybrany = wybor.get()

    if wybrany == 'szybowiec':
        modul_zera.wczytaj_wzorzec(modul_zera.wzorzec_szybowiec, 10, 10)
    elif wybrany == 'działo/szybowiec':
        modul_zera.wczytaj_wzorzec(modul_zera.wzorzec_dzialo_szybowiec, 10, 10)
    elif wybrany == 'losowy':
        modul_zera.losuj(modul_zera.model_siatki, modul_zera.szer, modul_zera.wys)

    aktualizacja()

def handler_start(zdarzenie):
    global uruchomiony, przycisk_start

    if uruchomiony:
        uruchomiony = False
        przycisk_start.configure(text='Start')
    else:
        uruchomiony = True
        przycisk_start.configure(text='Pauza')
        aktualizacja()

def handler_wyczysc(zdarzenie):
    global uruchomiony, przycisk_start

    uruchomiony = False
    for i in range(0, modul_zera.wys):
        for j in range(0, modul_zera.szer):
            modul_zera.model_siatki[i][j] = 0
    przycisk_start.configure(text='Start')
    aktualizacja()

def handler_siatki(zdarzenie):
    global widok_siatki, wielkosc_komorki

    x = int(zdarzenie.x / wielkosc_komorki)
    y = int(zdarzenie.y / wielkosc_komorki)

    if (modul_zera.model_siatki[x][y]==1):
        modul_zera.model_siatki[x][y] = 0
        narysuj_komorke(x,y, 'white')
    else:
        modul_zera.model_siatki[x][y] = 1
        narysuj_komorke(x, y, 'black')

def aktualizacja():
    global widok_siatki, okno_glowne, uruchomiony
    widok_siatki.delete(ALL)
    modul_zera.nastepne_pokolenie()

    for i in range(0, modul_zera.wys):
        for j in range(0, modul_zera.szer):
            if modul_zera.model_siatki[i][j] == 1:
                narysuj_komorke(i, j, 'black')
    if (uruchomiony):
        okno_glowne.after(100, aktualizacja)

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

if __name__== '__main__':
    ustawienia()
    modul_zera.losuj(modul_zera.model_siatki, modul_zera.szer, modul_zera.wys)
    aktualizacja()
    mainloop()
