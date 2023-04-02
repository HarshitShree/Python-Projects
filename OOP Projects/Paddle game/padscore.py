from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore=0
        self.lscore=0
        self.penup()
        self.goto(-5,250)
        self.color("white")
        self.write(f"{self.lscore}   {self.rscore}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    def ls(self):
        self.lscore+=1
        self.reset()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"{self.lscore}   {self.rscore}", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    def rs(self):
        self.rscore+=1
        self.reset()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"{self.lscore}   {self.rscore}", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()