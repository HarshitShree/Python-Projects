from turtle import Turtle, Screen
screen=Screen()
class Snake:
    def __init__(self):
        self.segment=[]
        self.crea()
    def west(self):
        if self.segment[0].heading()!=0:
            self.segment[0].setheading(180)
    def east(self):
        if self.segment[0].heading()!=180:
         self.segment[0].setheading(0) 
    def north(self):
        if self.segment[0].heading()!=270:
         self.segment[0].setheading(90)
    def south(self):
        if self.segment[0].heading()!=90:
         self.segment[0].setheading(270) 
    def movement(self):
        for i in range(len(self.segment)-1,0,-1):
            x=self.segment[i-1].xcor()
            y=self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.segment[0].forward(20)
        self.segment[len(self.segment)-1].color("white")
    def crea(self):
        for i in range(3):
            tim=Turtle()
            tim.shape("square")
            tim.color("white")
            tim.penup()
            self.segment.append(tim)
        self.segment[1].goto(-20,0)
        self.segment[2].goto(-40,0)
    def col(self):
        tim=Turtle()
        tim.shape("square")
        tim.penup()
        tim.speed(0)
        self.segment.append(tim)



