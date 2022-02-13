pelny = False

datki = []
limit = 45

zabawki = ['robot', 'lalka', 'pilka', 'puzzle']

while not pelny:
    for zabawka in zabawki:
        datki.append(zabawka)
        ilosc = len(datki)
        if (ilosc >= limit):
            pelny = True

print ('W koszyku znajduje się', len(datki), 'zabawek')
print(datki)
