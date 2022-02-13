def czy_to_palindrom(slowo):
    if len(slowo) <= 1:
        return True
    else:
        if slowo[0] == slowo[-1]:
            return czy_to_palindrom(slowo[1:-1])
        else:
            return False

slowa = ['atokanapapanakota', 'radar', 'jak', 'rador', 'kaijak']
for slowo in slowa:
    print(slowo, czy_to_palindrom(slowo))
