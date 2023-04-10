from turtle import Turtle
import random
colour=["red","green","gold","blue","orange","cyan","white","purple","light salmon"]
ycord=[-200,-180,-160,-140,-120,-100,-80,-60,-40,-20,0,200,180,160,140,120,100,80,60,40,20,-120,-100,-80,-60,-40,-20,0,200,180,160,140,120,-160,-140,-120,-100,-80,-60,-40,-20,0]
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-310,random.choice(ycord))
        self.color(random.choice(colour))
        self.shape("square")
        self.shapesize(1.2,1.6)
        self.speed("fastest")
     
    def movement(self,x):
        self.goto(self.xcor()+10,self.ycor())
        
        
        