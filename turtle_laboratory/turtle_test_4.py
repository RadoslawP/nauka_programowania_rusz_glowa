import turtle

powolniak = turtle.Turtle()
powolniak.shape('turtle')
powolniak.pencolor('blue')
powolniak.penup()
powolniak.setposition(-120,0)
powolniak.pendown()
powolniak.circle(50)

powolniak.pencolor('red')
powolniak.penup()
powolniak.setposition(120,0)
powolniak.pendown()
powolniak.circle(50)

turtle.mainlloop()
