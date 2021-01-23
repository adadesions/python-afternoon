# abstact.py
from turtle import *

bgcolor('black')
pencolor('yellow')
speed(0)
colors = ['red', 'blue', 'green', 'yellow']
def square(side):
    for i in range(4):
        forward(side)
        left(90)

for i in range(360):
    if i >= 0 and i <= 90:
        pencolor('red')
    elif i >= 90 and i <= 180:
        pencolor('green')
    elif i >= 180 and i <= 270:
        pencolor('blue')
    else:
        pencolor('yellow')
    square(i)
    right(7)

done()