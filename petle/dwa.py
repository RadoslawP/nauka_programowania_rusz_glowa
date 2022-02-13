for wyraz in ['aa', 'bbb', 'cccc', 'ddddd', 'eeeeee']:
    for i in range(2,7):
        litery = len(wyraz)
        if (litery%i) == 0:
            print(i, wyraz)
