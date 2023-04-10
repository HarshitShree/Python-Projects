from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,-250)
        self.color("white")
        self.shape("turtle")
        self.left(90)
    def move(self):
        self.goto(self.xcor(),self.ycor()+10)