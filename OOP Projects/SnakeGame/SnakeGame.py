#Basic
from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()
screen.tracer(0)
turtles=[]
snake=Snake()
food=Food()
writes=Score()
screen.update()
writes.score=0

#movement
screen.onkey(key="d", fun=snake.east)
screen.onkey(key="a", fun=snake.west)
screen.onkey(key="w", fun=snake.north)
screen.onkey(key="s", fun=snake.south)

#Snake movemnt speed
snake.segment[0].speed(1)
snake.segment[1].speed(0)
snake.segment[2].speed(0)



#Game movement
gameon=True
while gameon:
    #Food Cord
    x=food.foods[0].xcor()
    y=food.foods[0].ycor()
    
    #Base
    screen.update()
    time.sleep(0.1)
    snake.movement()
    
    #detection of out of bounds
    if snake.segment[0].xcor()>315 or snake.segment[0].xcor()<-315 :
        writes.gameover()
        print(f"Your final score is {writes.score}")
        gameon=False
    if snake.segment[0].ycor()>315 or snake.segment[0].ycor()<-315 :
        writes.gameover()
        print(f"Your final score is {writes.score}")
        gameon=False
    
    #Detection of tail collision
    for i in snake.segment[1:]:
        if snake.segment[0].distance(i) < 10:
            writes.gameover()
            print(f"Your final score is {writes.score}")
            gameon=False
            

    #detection of collision
    if snake.segment[0].distance(x,y) < 15:
        food.foods[0].goto(700,700)
        food=Food()
        snake.col()
        writes.score+=1
        writes.touchdown()

screen.exitonclick()



