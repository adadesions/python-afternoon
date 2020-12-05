import turtle

t = turtle.Pen()
t.pencolor('red')
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green', 'pink', 'purple']
t.speed(10)

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x/100+1)
    t.forward(x)
    t.left(45)

turtle.done()