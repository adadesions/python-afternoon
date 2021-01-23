from turtle import *

name = ' '
name_list = []
bgcolor('black')
colors = ['yellow', 'red', 'green', 'blue', 'pink', 'orange', 'white', 'purple']
speed(0)

while name != '':
    name = textinput('Name', 'What\'s your name ?')

    if name != '':
        name_list.append(name)

c_len = len(colors)
n_len = len(name_list)

for i in range(1000):
    pencolor(colors[i % n_len])
    penup()
    forward(i * n_len)
    pendown()
    write(name_list[i % n_len], font=('Arial', int(i/n_len), 'bold'))
    left(360/n_len + 2)

done()


#     for i in range(2):
#         write(name)
#         forward(30)

# print('Bye Byeeeeee~')
# print(name_list)