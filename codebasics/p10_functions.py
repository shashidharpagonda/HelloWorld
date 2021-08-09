
#1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
#   Equation of an area of a triangle is,
#   area = (1/2)*base*height

def areaTriangle(base, height,shapetype='triangle'):
    if shapetype=='triangle':
        area = (1/2)* base * height
    if shapetype=='rectangle':
        area = base * height
    else:
        area = 'None'
    return area

print(areaTriangle(10,20,'rectangle'))
print(areaTriangle(10,20)) #Since we are not passing shape type. It will consider it as triangle

#2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
#   Based on shape type it will calculate area. Equation of rectangle's area is,
#   rectangle area=length*width
#   If no shape is supplied then it should take triangle as a default shape



#3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
"""
    *
    **
    ***
"""
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
def pattern_shape(len=5):
    for i in range(len+1):
        s=''
        for j in range(i):
            s+='*'
        print(s)

#len=int(input('Enter the size for pattern: '))

pattern_shape()