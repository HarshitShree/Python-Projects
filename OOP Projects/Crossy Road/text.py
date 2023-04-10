from turtle import Turtle
class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.score=0
        self.highscore=0
        self.penup()
        self.goto(-290,240)
        self.color("white")
        self.write(f"Level {self.level}", align="Left", font=("Arial", 24, "normal"))
        self.goto(+290,240)
        self.color("white")
        self.write(f"Highscore = {self.highscore}", align="Right", font=("Arial", 24, "normal"))
        self.hideturtle()
        
        
    def touchdown(self):
        self.reset()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"Level {self.level} cleared", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.score+=1
        self.level+=1
        
    def nextlevel(self):
        self.reset()
        self.goto(-290,240)
        self.color("white")
        self.write(f"Level {self.level}", align="Left", font=("Arial", 24, "normal"))
        self.penup()
        self.goto(+290,240)
        self.color("black")
        self.color("white")
        self.write(f"Highscore = {self.highscore}", align="Right", font=("Arial", 24, "normal"))
        self.hideturtle()
     
   

    def gameover(self):
        if self.score>self.highscore:
            self.highscore=self.score
            self.reset()
            self.penup()
            self.goto(0,270)
            self.color("white")
            self.write("Game Over", True, align="center", font=("Arial", 24, "normal"))
            self.penup()
            self.goto(0,235)
            self.color("white")
            self.write(f"Final score = {self.score}, a new highscore!", True, align="center", font=("Arial", 24, "normal"))
            self.score=0
            self.level=1
            self.hideturtle()
            
        else:
            self.reset()
            self.penup()
            self.goto(0,270)
            self.color("white")
            self.write("Game Over", True, align="center", font=("Arial", 24, "normal"))
            self.goto(0,235)
            self.color("white")
            self.write(f"Final score = {self.score}", True, align="center", font=("Arial", 24, "normal"))
            self.score=0
            self.level=1
            self.hideturtle()
            
            
            