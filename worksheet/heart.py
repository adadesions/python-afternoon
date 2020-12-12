from turtle import *

bgcolor('black')
pencolor('pink')

line = 37
width(2)

left(30)
forward(150)
for i in range(line):
    left(5)
    forward(10)

pu()
goto(0, 0)
pd()
setheading(180)

right(30)
forward(150)
for i in range(line):
    right(5)
    forward(10)


done()