from turtle import *

bgcolor('black')
pencolor('yellow')
speed(0)
num = numinput("Input", "Enter a number")

if num == 0:
    for i in range(360):
        right(1)
        fd(3)
elif num == 1:
    left(45)
    fd(100)
    setheading(270)
    fd(400)
    setheading(0)
    fd(100)
    backward(200)
elif num == 2:
    fd(300)
    right(135)
    fd(360)
    setheading(0)
    fd(300)
elif num == 3:
    penup()
    setpos((0, 300))
    pendown()
    for i in range(180):
        fd(2)
        right(1)
    setheading(0)
    for i in range(200):
        fd(2)
        right(1)

done()