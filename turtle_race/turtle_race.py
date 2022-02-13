#importowanie potrzebnych modułów
import turtle
import random

#żółwie przechowujemy w liście
zolwie = list()

#definiujemy funkcję ustawiającą żółwie na starcie
def ustawienia():
    global zolwie
    start = -620
    #ustawienia ekranu startowego
    ekran = turtle.Screen()
    ekran.setup(1290, 720)
    ekran.bgpic('pavement.gif')

    #tworzymy listy początkowych ustawień żółwi
    zolw_pion = [-40, -20, 0, 20, 40, 60]
    zolw_kolor = ['blue', 'red', 'purple', 'yellow', 'green', 'orange']

    #iterujemy po ilości wymienionych pozycji startowych żółwi
    for i in range(0, len(zolw_pion)):
        #w każdej iteracji tworzony jest kolejny żłów
        nowy_zolw = turtle.Turtle()
        nowy_zolw.shape('turtle')
        nowy_zolw.penup()
        #nadajemy żłówiowi jego pozycję startową i kolor
        nowy_zolw.setpos(start, zolw_pion[i])
        nowy_zolw.color(zolw_kolor[i])
        nowy_zolw.pendown()
        #nowego żłówie dodajemy do globalnej listy
        zolwie.append(nowy_zolw)

#definiujemy funkcję odpowiadającą za wyścig
def wyscig():
    global zolwie
    #warunek trwania gry to wyłonienie zwycięzcy
    zwyciezca = False
    #zmienna lokalna przechowująca współrzędną osi x mety
    meta = 590

    #pętla będzie toczyła wyścig dopuki nie wyłonimy zwycięzcy
    while not zwyciezca:
        #z każdą pętla, każdy żółw po koleji dostaje możliwość poruszenia się
        for biezacy_zolw in zolwie:
            #generujemy liczbę losową, która poruszy żółwia do przodu
            ruch = random.randint(0,2)
            biezacy_zolw.forward(ruch)

            #pobieramy współrzędną x żółwia
            xcor = biezacy_zolw.xcor()
            #porównujemy współrzędną żółwia ze współrzędną mety
            if (xcor >= meta):
                #po wyłonieniu zwycięzcy pobieramy kolor żółwia
                zwyciezca = True
                kolor_zwycięzcy = biezacy_zolw.color()
                #ogłoszenie koloru zywcięzcy
                print('Zwycięzcą jest żółw', kolor_zwycięzcy[0])

#wywołujemy ustawienia żółwi na starcie
ustawienia()
#wywołujemy funkcję wyścig
wyscig()

turtle.mainloop()
