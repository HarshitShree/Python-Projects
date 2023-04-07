from turtle import Turtle
class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.posx=-280
        self.posy=280
    def writer(self,txt):
        self.penup()
        self.goto(self.posx,self.posy)
        self.color("white")
        self.write(f"{txt}", True, align="left", font=("Arial", 12, "normal"))
        self.hideturtle()
        self.posy-=20
