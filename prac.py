from turtle import Turtle, Screen

ted = Turtle()
ted.shape("circle")
sali=Turtle()
sali.color("black")
sali.goto(370,270)
ted.left(36.11934085)
gam_on=True
while gam_on:
    while ted.distance(sali) > 1 :
        if ted.distance(sali) == 1:
            gam_on =False
        else:
            ted.forward(100)



screen = Screen()
screen.exitonclick()