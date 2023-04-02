from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(cords)
    def up(self):
        self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        self.goto(self.xcor(),self.ycor()-20)
        