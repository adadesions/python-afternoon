from turtle import *

bgcolor('black')
pencolor('yellow')

_len = 45
for i in range(_len):
    forward(i)
    left(8)
pu()
goto(0, 0)
left(-1)
pd()
for i in range(_len):
    forward(i)
    right(8)

done()