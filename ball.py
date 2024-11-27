from turtle import Turtle


class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color("white")
        self.goto(0, 0)
        self.penup()

    def move(self):
        new_x = self.xcor()+10
        new_y = self.ycor()+10
        self.goto(new_x, new_y)

    def bounce(self):
        new_x = self.xcor() + 20
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)



