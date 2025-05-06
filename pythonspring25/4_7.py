import turtle
from random import randint

turtle.colormode(255)

# screen setup
window = turtle.Screen()

window.bgcolor(randint(0,255),randint(0,255),randint(0,255))
window.setup(400,400) #does not work on trinket
window.title("eRiC's PiThOnE turdl skrein") #does not work on trinket
##############

# setup "turtle"
leo = turtle.Turtle()
leo.pencolor(0,0,255)
leo.fillcolor(randint(0,255),randint(0,255),randint(0,255))
leo.shape("turtle") #circle, triangle, square, arrow
leo.shapesize(1,1,1) #does not work on trinket
leo.speed(0)
##############

# functions
def move(x,y):
    leo.penup()
    leo.goto(x,y)
    leo.pendown()
    return

def square(size,sides):
    for i in range(sides):
        leo.forward(size)
        leo.left(360/sides)
    return
##############

# turtle actually moving
for i in range(10):
    move(-200+i*25,-200+i*25)
    square(400-i*50,4)
