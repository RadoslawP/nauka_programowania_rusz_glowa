uzytkownicy={}
uzytkownicy['Kasia']={'email': 'kasia@przykład.com', 'plec': 'k', 'wiek': 27, 'przyjaciele': ['Jan', 'Jacek']}
uzytkownicy['Jan']={'email': 'jan@przykład.com', 'plec': 'm', 'wiek': 24, 'przyjaciele': ['Kasia', 'Jacek']}
uzytkownicy['Jacek']={'email': 'jacek@przykład.com', 'plec': 'm', 'wiek': 32, 'przyjaciele': ['Kasia']}

max=1000
for imie in uzytkownicy:
    uzytkownik=uzytkownicy[imie]
    przyjaciele=uzytkownik['przyjaciele']
    if len(przyjaciele)<max:
        najbardziej_aspoleczny=imie
        max=len(przyjaciele)

print('Najbardziej aspolecznym uzytkownikiem jest', najbardziej_aspoleczny)
