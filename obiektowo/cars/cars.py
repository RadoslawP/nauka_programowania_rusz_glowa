class Samochod():
    def __init__(self):
        self.szybkosc = 0
        self.uruchomiony = False

    def uruchomienie(self):
        self.uruchomiony = True

    def jazda(self):
        if self.uruchomiony:
            print('Samochód jedzie')
        else:
            print('Najpierw uruchom silnik')

class Taksowka(Samochod):
    def __init__(self):
        Samochod.__init__(self)
        self.pasazer = None
        self.oplata = 0.0

    def jazda(self):
        print('Z drogi!')
        Samochod.jazda(self)

    def zamowienie(self, pasazer):
        print('Taksówka zamówiona przez', pasazer)
        self.pasazer = pasazer

    def placenie(self, kwota):
        print('Należność', kwota)
        self.oplata = self.oplata + kwota
        self.pasazer = None

class Limuzyna(Taksowka):
    def __init__(self):
        Taksowka.__init__(self)
        self.szyberdach = 'zamkniety'

    def jazda(self):
        print('Jedziemy luksusowo!')
        Samochod.jazda(self)

    def placenie(self, kwota, napiwek):
        print('Należność', kwota, 'Napiwek', napiwek)
        Taksowka.placenie(self, kwota + napiwek)

    def nalej_drinka(self):
        print('Nalewam drinka')

    def otworz_szyberdach(self):
        print('Otwieram szyberdach')
        self.szyberdach = 'otwarty'

    def zamknij_szyberdach(self):
        print('Zamykam szyberdach')
        self.szyberdach = 'zamknięty'

samochod = Samochod()
takstowka = Taksowka()
limuzyna = Limuzyna()

samochod.uruchomienie()
samochod.jazda()

takstowka.uruchomienie()
takstowka.zamowienie('Kasia')
takstowka.jazda()
takstowka.placenie(5.0)

limuzyna.uruchomienie()
limuzyna.zamowienie('Jacek')
#takstowka.jazda()
limuzyna.nalej_drinka()
limuzyna.placenie(10.0, 5.0)
