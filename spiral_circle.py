import turtle

t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'green']
t.speed(0)
for x in range(100):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(1)

turtle.done()