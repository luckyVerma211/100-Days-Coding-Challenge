import turtle
t=turtle.Turtle()

t.begin_fill()
t.color("red","green")
for i in range(4):
    t.forward(200)
    t.left(90)
t.end_fill()
c=["blue","red","orange","yellow","cyan"]
k=0
for i in range(100,0,-20):
    t.color(c[k])
    k+=1
    t.begin_fill()
    t.circle(i)
    t.end_fill()
turtle.done()