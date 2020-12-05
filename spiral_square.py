import turtle

t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'green', 'blue', 'pink', 'gray']
t.speed(0)
sides = 6

for x in range(500):
    t.pencolor(colors[x % sides])
    t.forward(x * 3/sides + x)
    t.left(90 + 360/sides + 1)
    t.width(x * sides/200)
    # t.left(90)

turtle.done()