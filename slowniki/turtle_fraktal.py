import turtle

def ustawienia(pisak):
    pisak.color('blue')
    pisak.penup()
    pisak.goto(-200, 100)
    pisak.pendown()

def koch(pisak, rozmiar, skala):
    if skala == 0:
        pisak.forward(rozmiar)
    else:
        for kat in [60, -120, 60, 0]:
            koch(pisak, rozmiar/3, skala-1)
            pisak.left(kat)

def main():
    pisak = turtle.Turtle()
    ustawienia(pisak)
    turtle.tracer(100)

    skala = 5
    rozmiar = 400

    for i in range(3):
        koch(pisak, rozmiar, skala)
        pisak.right(120)

if __name__ == '__main__':
    main()
    turtle.tracer(100)
    turtle.mainloop()
