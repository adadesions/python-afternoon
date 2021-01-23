# Question 2

from turtle import *

bgcolor('black')
pencolor('yellow')

# Pentagon
for i in range(5):
    forward(50)
    left(72)
    forward(50)

pu()
goto(-300, 100)
pd()
pencolor('blue')

# Haxagon
for i in range(6):
    forward(60)
    left(360/6)
    forward(60)

pu()
goto(-300, -300)
pd()
pencolor('red')

# Octagon
for i in range(8):
    forward(80)
    left(360/8)
    forward(80)

done()
