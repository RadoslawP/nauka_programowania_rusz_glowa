import turtle

powolniak = turtle.Turtle()
powolniak.shape('turtle')

def narysuj_ksztalt(zolw, boki):
    kat = 360/boki
    for i in range(0, boki):
        zolw.forward(100)
        zolw.right(kat)

narysuj_ksztalt(powolniak,3)
narysuj_ksztalt(powolniak,5)
narysuj_ksztalt(powolniak,8)
narysuj_ksztalt(powolniak,10)

turtle.mainlloop()
