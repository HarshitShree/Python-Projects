#Basics
from turtle import Turtle
from turtle import Screen
import random
screen = Screen()
screen.screensize(500,400)
ycord=[-60,-30,0,30,60]
colour=['red','cyan','blue','black','gold']
turtles=[]
move=[5,6,7,8,9,8,6,7,15,12]
on=True

#Bet
player=screen.textinput("Bet", "Which colour do you want to bet on")
#Turtle creation
for i in range(5):
    tim=Turtle()
    tim.penup()
    tim.shape("turtle")
    tim.goto(-280,ycord[i])
    tim.color(colour[i])
    turtles.append(tim)

#Finish line
fin=Turtle()
fin.penup()
fin.goto(320,90)
fin.pendown()
fin.right(90)
fin.forward(180)
fin.hideturtle()


#Turtle movement and end
while on:
    for i in turtles:
        i.forward(random.choice(move))
        if i.xcor()>=304:
            on=False
            col=i.pencolor()
            break
print(f"The winning turtle is the {col} turtle ")
if player==col:
    print("You have won")
else:
    print("You have lost")
    
    
    
screen.exitonclick()


