import turtle

#screen setup
screen = turtle.Screen()
screen.setup(400,400)
screen.bgcolor("indian red")
#############

#setup turtle
donny = turtle.Turtle()
donny.shape("turtle") 
donny.fillcolor("SlateBlue2")
donny.pencolor("green2")
donny.shapesize(1,1,2) 
donny.speed(0)
#############

#functions
def step():
    donny.forward(20)
    if donny.xcor()>200: #right edge
      move(-200,donny.ycor())
    elif donny.xcor()<-200: #left edge
      move(200,donny.ycor())
    if donny.ycor()>200: #top edge
      move(donny.xcor(),-200)
    elif donny.ycor()<-200: #bottom edge
      move(donny.ycor(),200)
    screen.ontimer(step,100)
    return

def turnL():
    donny.left(10)
    return

def turnR():
    donny.right(10)
    return

def move(x,y):
    donny.penup()
    donny.goto(x,y)
    donny.pendown()
    return
#############

#key press stuff
screen.onkey(step,"w")
screen.onkey(turnL,"a")
screen.onkey(turnR,"d")
screen.listen()

screen.mainloop() 