from turtle import Turtle
class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
    def cor(self,cords,Guess):
        cord=eval(cords)
        xcord=int(cord[0])
        ycord=int(cord[1])
        self.color("Blue")
        self.penup()
        self.goto(xcord,ycord)
        self.write(f"{Guess}", True, align="center", font=("Arial", 10, "normal"))
        self.hideturtle()
        self.score+=1
    def incor(self):
        xcord=-15
        ycord=0
        self.penup()
        self.goto(xcord,ycord)
        self.color("black")
        self.write(f"Final Score={self.score}", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
   