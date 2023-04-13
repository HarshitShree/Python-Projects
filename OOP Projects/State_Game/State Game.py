#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import pandas as pd
#import turtle
#from turtle import Turtle,Screen
#screen=Screen()
#screen.title("Indian States Game")
#gif="C:/Users/Harshit Shree/Downloads/Indianmap.gif"
#screen.addshape(gif)
#turtle.shape(gif)

#def getcord(x,y):
#    print(x,y)
#screen.onscreenclick(getcord)
#turtle.mainloop()


# In[23]:


#dict={
    #"state":["Himachal Pradesh","Punjab","Haryana","Rajasthan","Gujurat","Madhya Pradesh","Maharashtra","Goa","Karnataka","Kerela","Tamil Nadu","Andhra Pradesh","Telangana","Odisha","Chattisgarh","Jharkhand","West Bengal","Bihar","Uttar Pradesh","Sikkim","Assam","Arunachal Pradesh","Nagaland","Manipur","Mizoram","Tripura","Meghalaya","Uttrakhand"],
    #"Cords":[[-68.0,153.0],[-99.0,137.0],[-81.0,112.0],[-120.0,75.0],[-148.0,27.0],[-65.0,25.0],[-100.0,-34.0],[-123.0,-97.0],[-94.0,-116.0],[-89.0,-164.0],[-53.0,-166.0],[-38.0,-96.0],[-42.0,-61.0],[36.0,-18.0],[-7.0,-7.0],[39.0,32.0],[74.0,22.0],[48.0,61.0],[-28.0,74.0],[79.0,91.0],[141.0,74.0],[169.0,115.0],[166.0,74.0],[156.0,54.0],[146.0,31.0],[127.0,38.0],[200,200],[-70,135]]
#}


# In[24]:


#data=pd.DataFrame(dict)
#data.to_csv("C:/Users/Harshit Shree/Downloads/Project.csv")


# In[1]:


#Basic
import pandas as pd
import turtle
from turtle import Turtle,Screen
import time

#Screen
screen=Screen()
screen.title("Indian States Game")
screen.bgcolor("Black")
gif="C:/Users/Harshit Shree/Downloads/Indianmap.gif"
screen.addshape(gif)
turtle.shape(gif)

#Text
from Stategametext import Write
text=Write()

#File
df=pd.read_csv("C:/Users/Harshit Shree/Downloads/Project.csv")
states_list=df.state.to_list()

#Game
gameon=True
while gameon:
    guess=screen.textinput("Guess a State","Type exit to leave")
    if guess in states_list:
        cord=df[df.state==guess].Cords.values[0]
        text.cor(cord,guess)
        time.sleep(1)
    elif guess=="exit":
        text.incor()
        gameon=False
    else:
        time.sleep(1)
        
    #else:
        #text.incor()
        #time.sleep(1)

screen.exitonclick()

