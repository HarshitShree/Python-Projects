#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic
from text import Text
from car import Car
from player import Player
import time
from turtle import Screen,Turtle

#Screen
screen=Screen()
screen.setup(600,630)
screen.bgcolor("black")
screen.title("Crossy Road")
screen.tracer(0)
screen.listen()

#Variables
car=[]
num=0
speed=5
diffi=4

#Text
bot=Text()

#Lines
tim=Turtle()
tim.penup()
tim.goto(-315,230)
tim.pendown()
tim.pencolor("white")
tim.goto(+315,230)
tim.penup()
tim.goto(-315,-230)
tim.pendown()
tim.goto(315,-230)

#Level display


#player
turtle=Player()
screen.onkey(key="w", fun=turtle.move)


#Game
gameon=True
while gameon:
    #Car
    if num%diffi==0:
        cars=Car()
        car.append(cars)
    num+=1
    #Optimization
    if num%100==0:
        car=car[10:]
        
    #General
    for i in car:
        i.movement(speed)
    screen.update()
    time.sleep(0.1)
    
    #collision
    for i in car:
        if turtle.distance(i) < 30:
            gameon=False
            bot.gameover()
    
    #Finish line
    if turtle.ycor()>=242:
        bot.touchdown()
        time.sleep(2)
        bot.nextlevel()
        turtle.goto(0,-250)
        screen.update()
        speed+=5
        if speed%3==0:
            diffi-=1
        
        
    
screen.exitonclick()


# In[ ]:





# In[ ]:




