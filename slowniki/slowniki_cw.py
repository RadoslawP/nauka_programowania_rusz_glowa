moj_slownik = {}
moj_slownik['joanna']='867-5309'
moj_slownik['dawid']='321-6617'
moj_slownik['jerzy']='771-0091'

numer_telefonu=moj_slownik['joanna']

if 'joanna' in moj_slownik:
    print('Znalazła się:', moj_slownik['joanna'])
else:
    print('Numer telefonu Joanny:', numer_telefonu)

for klucz in moj_slownik:
    print(klucz, ':', moj_slownik[klucz])

harry={'imie': 'Harry',
       'nazwisko': 'Potter',
       'dom': 'Gryffindor',
       'przyjaciele': ['Ron', 'Hermoina'],
       'rok_urodzenia': 1980}

print(harry)
