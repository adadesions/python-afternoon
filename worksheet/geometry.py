# Geometry.py

# Tasks
# Write these functions to calculate following tasks
# 1. Areas ==> Circle, Triangle, Reactangle, Square,..
# 2. Volumes ==> Sphere, Pyramid, Prism, Cone, 
def rectangle(width, length):
    return width * length

def perimeter_rect(width, length):
    return 2*width + 2*length

def triangle(base, height):
    return 0.5 * base * height

def perimeter_triangle(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print("Geometry.py")
    area_rect = rectangle(10, 100)
    peri_rect = perimeter_rect(10, 100)
    area_tri = triangle(30, 60)
    peri_tri = perimeter_triangle(10, 20, 30)
    print(f'Area of React = {area_rect} unit sqrt.')
    print(f'Perimeter of React = {peri_rect} unit.')
    print('='*50)
    print(f'Area of Triangle = {area_tri} unit sqrt')
    print(f'Perimeter of Triangle = {peri_tri} unit')