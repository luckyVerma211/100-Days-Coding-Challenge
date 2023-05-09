import turtle
import time 

def moveleft():
    xb=ball.xcor()
    ball.setx(xb-10)

def moveright():
    xb=ball.xcor()
    ball.setx(xb+10)

wn=turtle.Screen()
wn.title("Bouncing Ball")
wn.bgcolor("cyan")

wn.setup(width=600,height=600)

ball=turtle.Turtle()

ball.color("red")
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=6,stretch_len=6)
ball.penup()


h=0
while True:
    if h==0:
        moveright()
    if h==1:
        moveleft()
    if ball.xcor()>=300:
        h=1
    if ball.xcor()<=-300:
        h=0
    time.sleep(0.1)
    wn.update()


