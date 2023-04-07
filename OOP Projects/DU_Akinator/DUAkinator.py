#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Base
from turtle import Turtle,Screen
from writer import Write
import time
chetan=Write()
#I know about the spelling mistake, im too lazy to change it
screeen=Screen()
screeen.setup(600,600)
screeen.bgcolor("black")
screeen.title("Delhi University Akinator")
Question="Question"
screeen.tracer(0)

### It is only made for a few select colleges  ###
print("Welcome to Delhi University akinator")
print(" ")
chetan.writer("It is a north campus college, yes or no?")
screeen.update()
time.sleep(0.5)
NC = screeen.textinput(Question,"It is a north campus college, yes or no \n")
chetan.writer(NC)
screeen.update()
time.sleep(0.5)
if NC == "yes":
  chetan.writer("It is a women only college, yes or no?")
  screeen.update()
  time.sleep(0.5)
  NCW = screeen.textinput(Question,"It is a women only college, yes or no \n")
  chetan.writer(NCW)
  screeen.update()
  time.sleep(0.5)
  if NCW == "yes":
    chetan.writer("The college is Miranda House")
  if NCW == "no":  
    NCM = screeen.textinput(Question,"Does the name of the college start with S, yes or no \n")
    if NCM == "yes":
      NAA = screeen.textinput(Question,"The college only offers two  courses, yes or no \n")
      if NAA == "yes":
        print("The college is Shri Ram College of  Commerce")
      else:
        SMC = screeen.textinput(Question,"It is a Sikh Minority college?, yes or no \n")
        if SMC == "yes":
          SMCF = screeen.textinput(Question,"The college has 'Commerce'in its name, yes or no \n")
          if SMC == "yes":
            if SMCF == "no":
              print("The college is SGTB Khalsa")
            else:
              print("The college is Sri Guru Gobind College of Commerce")
        else:
          print("The college is St. Stephens")
    if NCM == "no":
      HC = screeen.textinput(Question,"Does the name of the college start with H, yes or no \n")
      if NCM == "no":
        if HC == "yes":
          HCHIN = screeen.textinput(Question,"The college has the name of religion in its name, yes or no \n")
          if  HCHIN == "yes":
            print("The college is Hindu College")
          else:
            print("The college is Hansraj College")  
    if NCM == "no":
      if HC == "no":
        Ramjas = screeen.textinput(Question,"The name of the college starts with R, yes or no \n")
        if  Ramjas == "yes":
          print("The college is Ramjas College")
    if NCM == "no":
      if HC == "no":
        if Ramjas == "no":
          DC = screeen.textinput(Question,"The name of the college starts with D, yes or no \n")
          if DC == "yes":
            Eco = screeen.textinput(Question,"The college has 'Economics' in its name, yes or no \n")
            if Eco == "yes":
              print("The college is Delhi School of Economics")
            else:
              print("The college is Dalaut Ram College")
if NC == "no":
  chetan.writer("It is a south campus college, yes or no?")
  screeen.update()
  time.sleep(0.5)
  SC = screeen.textinput(Question,"It is a south campus college, yes or no \n")
  chetan.writer(SC)
  screeen.update()
  time.sleep(0.5)
  if SC == "yes":
    chetan.writer("It is a women only college, yes or no?")
    screeen.update()
    time.sleep(0.5)
    SCW = screeen.textinput(Question,"It is a women only college, yes or no \n")
    chetan.writer(SCW)
    screeen.update()
    time.sleep(0.5)
    if SCW == "yes":
      LSR = screeen.textinput(Question,"The name of the college starts  with L, yes or no \n")
      if LSR == "yes":
        print("The name of the college is Lady Shri Ram College")
      else:
        print("The name of the college is Kamala Nehru College")
    if SCW != "yes":
      chetan.writer("The name of the college starts with A, yes or no?")
      screeen.update()
      time.sleep(0.5)
      SCA = screeen.textinput(Question,"The name of the college starts with A, yes or no \n")
      if SCA == "yes":
        chetan.writer(SCA)
        screeen.update()
        time.sleep(0.5)
        chetan.writer("The college is named after an Indian mathematician, yes or no?")
        screeen.update()
        time.sleep(0.5)
        Arya = screeen.textinput(Question,"The college is named after an Indian mathematician, yes or no \n")
        if Arya ==  "yes":
         chetan.writer(Arya)
         screeen.update()
         time.sleep(0.5)
         chetan.writer("The college is Aryabhatta college")
        else:
          print("The college is Atma Ram Sanatan Dharma College") 
      if SCA == "no":
        print("The college is Sri Venkateshwara College")
if NC == "no":
  if SC == "no":
    chetan.writer("It is a off campus college, yes or no?")
    screeen.update()
    time.sleep(0.5)
    OC = screeen.textinput(Question,"It is a off campus college, yes or no \n")
    if OC == "yes":
      chetan.writer(OC)
      screeen.update()
      time.sleep(0.5)
      chetan.writer("The name of the college start with S, yes or no?")
      screeen.update()
      time.sleep(0.5)
      S = screeen.textinput(Question,"The name of the college start with S, yes or no \n")
      if S == "yes":
        chetan.writer(S)
        screeen.update()
        time.sleep(0.5)
        chetan.writer("The college is named after a medieval warrior, yes or no?")
        screeen.update()
        time.sleep(0.5)
        Shi = screeen.textinput(Question,"The college is named after a medieval warrior, yes or no \n")
        if Shi == "yes":
          chetan.writer(Shi)
          screeen.update()
          time.sleep(0.5)
          chetan.writer("The college is Shivaji College")
          screeen.update()
          time.sleep(0.5)
        else:
            if Shi != "yes":
              Sha = screeen.textinput(Question,"The college is named after a freedom fighter, yes or no \n")
            if Sha == "yes":
              print("The name of the college is Shaheed Bhagat Singh College of Business")
            if Sha == "no":
              SA = screeen.textinput(Question,"The college is named after an Indian philosopher, yes or no \n")
            if SA == "yes":
                print("The college is Sri Aurobindo College")
        if S == "no":
              R = screeen.textinput(Question,"The name of the college starts with R, yes or no \n")
              if R == "yes":
                Rama = screeen.textinput(Question,"The college is named after an Indian Mathematician, yes or no \n")
                if Rama == "yes":
                  print("The name of the college is Ramanujan College")
                else:
                  print("The college is Rajdhani College")
if NC == "no":
  if SC == "no":
    if OC == "no":
        chetan.writer("Bruh what?")
        screeen.update()
screeen.exitonclick()


# In[ ]:




