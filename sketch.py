from turtle import Turtle
from turtle import Screen
tim=Turtle()
tim.shape("turtle")
tim.color("cyan")
screen = Screen()
screen.listen()
tim.pensize(5)
def forward():
    tim.forward(10)
def backward():
    tim.backward(10)
def left():
    tim.left(10)
def right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=right)
screen.onkey(key="d", fun=left)    
screen.onkey(key="c", fun=clear)

screen.exitonclick()
