from turtle import *

def circle(h, k, r):
    points = []

    for x in range(-r, r):
        y = (r**2 - (x - h)**2)**0.5 + k
        points.append((x, y))
    
    return points

for p in circle(0, 0, 10):
    print(p)