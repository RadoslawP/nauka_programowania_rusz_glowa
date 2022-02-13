filmy = []
film = {}

film['tytul']='Zakazana planeta'
film['rok']=1957
film['ocena']='*****'
film['rok']=1956

filmy.append(film)

film2={'tytul': 'Byłem nastoletnim wilkołakiem', 'rok': 1957, 'ocena': '****'}
film2['ocena']='***'

filmy.append(film2)
filmy.append({'tytul': 'Kobiety wikingowie i wąż morski', 'rok': 1957, 'ocena': '**'})
filmy.append({'tytul': 'Zawrót głowy', 'rok': 1958, 'ocena': '*****'})

print('Polecane filmy')
print('------------------------------')
for film in filmy:
    if len(film['ocena']) >= 4:
        print(film['tytul'], '('+ film['ocena']+')', film['rok'])
