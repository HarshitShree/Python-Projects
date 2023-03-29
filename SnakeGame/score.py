from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"Score= {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        
    def touchdown(self):
        self.reset()
        self.penup()
        self.goto(0,250)
        self.color("white")
        self.write(f"Score= {self.score}", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    
    def gameover(self):
        self.reset()
        self.penup()
        self.goto(-12,30)
        self.color("white")
        self.write("Game Over", True, align="center", font=("Arial", 24, "normal"))
        self.goto(-15,0)
        self.color("white")
        self.write(f"Final score={self.score}", True, align="center", font=("Arial", 24, "normal"))
        
        
    
    
        
        
        






