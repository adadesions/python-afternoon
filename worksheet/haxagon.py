# Question 4

from turtle import *

bgcolor('black')
pencolor('yellow')
width(5)

for i in range(6):
    forward(100)
    left(360/6)

left(360/6)
forward(200)

for i in range(4):
    if i % 2 == 0:
        side = 100
    else:
        side = 200

    left(2*360/6)
    forward(side)

done()