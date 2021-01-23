# Rosette.py

from turtle import *

speed(0)
bgcolor('black')
pencolor('yellow')
n_circle = int(numinput('Number of Circle', 'How many circle?'))
colors = ['yellow', 'red', 'green', 'blue']

# Loops
for i in range(n_circle):
    pencolor(colors[0])
    circle(200)

    pencolor(colors[1])
    circle(150)
    
    pencolor(colors[2])
    circle(120)
    
    pencolor(colors[3])
    circle(37)

    left(360/n_circle)

done()