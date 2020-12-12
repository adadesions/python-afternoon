from turtle import *

bgcolor('black')
pencolor('yellow')

# forward(100)
# setheading(90)
# left(23)
# forward(100)
# setheading(45)
# forward(100)
speed(0)
# Function!!!!
def star(length):
    forward(length)
    for i in range(4):
        right(48*3)
        forward(length)

star(300)
pu()
goto(-100, 100)
pd()
star(100)

for i in range(300):
    star(i*2)
    left(180)


done()