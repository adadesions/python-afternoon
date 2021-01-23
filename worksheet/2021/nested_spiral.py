# nested_spiral.py
from turtle import *

bgcolor('black')
colors = ['yellow', 'red', 'green', 'blue', 'pink', 'orange', 'white', 'purple']
width(1)
speed(0)

def spiral(side, round):
    for i in range(int(round/2)):
        pencolor(colors[i % side])
        # pencolor(colors[0])
        forward(i * 2)
        left(360/side + 2)

side = 4
for i in range(100):
    penup() 
    forward(i * 4)
    pos = position()
    head = heading()

    print(pos, head)

    pendown()
    spiral(side, i)

    setpos(pos)
    setheading(head)
    left(360/side + 8)

done()