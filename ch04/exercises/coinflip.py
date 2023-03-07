import turtle
import random

turtle1 = turtle.Turtle()
screen = turtle.screensize()
print(screen)
is_in_screen = True

while is_in_screen == True:
    coin = random.randint(1,2)
    if coin == 1:
        turtle1.left(90)
        turtle1.forward(50)
    elif coin == 2:
        turtle1.right(90)
        turtle1.forward(50)
    (x,y)= turtle1.xcor(),turtle1.ycor()
    if (x,y) >(400,300):
        is_in_screen == False



