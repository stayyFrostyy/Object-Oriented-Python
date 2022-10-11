
# Attempting to use the turtle class.

# This imports the turtle library
from turtle import *

scr = getscreen()
t = Turtle()

def square():
    for i in range(4):
        forward(100)
        right(90)
        speed(0)
    
def circleSquare():
    for i in range(360):
        square()
        right(1)
        speed(0)

t.backward(150)
t.right(90)
t.circle(150)

circleSquare()


