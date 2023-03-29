from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super(Turtle).__init__()
        self.foods=[]
        self.crea()
    def crea(self):
        rat=Turtle()
        rat.shape("circle")
        rat.penup()
        rat.turtlesize(0.5, 0.5)
        rat.color("blue")
        rat.speed("fastest")
        randx=random.randint(-280, 280)
        randy=random.randint(-280, 280)
        rat.goto(randx,randy)
        self.foods.append(rat)