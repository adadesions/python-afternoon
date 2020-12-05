# Question 3 - no_corners.py

from turtle import *

bgcolor('black')
pencolor('yellow')
width(5)

for i in range(4):
    if i % 2 == 0:
        side = 250
    elif i % 2 > 10:
        print("A")
    else:
        side = 150
    forward(side)
    pu()
    forward(10)
    left(90)
    forward(10)
    pd()

done()
