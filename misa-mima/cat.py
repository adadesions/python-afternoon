from turtle import *

bgcolor('black')
pencolor('orange')
width(5)

circle(200)
penup()
goto(-150, 250)
pendown()

# Semi-circle
left(45)
for i in range(18):
    forward(4)
    right(i)

penup()
goto(150, 250)
pendown()
forward(100)

done()