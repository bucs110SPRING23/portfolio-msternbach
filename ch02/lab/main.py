import random
import turtle
import pygame
import math

window = turtle.Screen()

#race 1
distance1 = random.randint(1,100)
distance2 = random.randint(1,100)
# print(distance1,distance2)

turtle1 = turtle.Turtle()
turtle1.color("orange")
turtle1.penup()
turtle1.speed(2)
turtle1.goto(-100,20)
turtle1.forward(distance1)
turtle2 = turtle.Turtle()
turtle2.color("pink")
turtle2.penup()
turtle2.speed(2)
turtle2.goto(-100,-20)
turtle2.forward(distance2)
turtle1.goto(-100,20)
turtle2.goto(-100,-20)

for i in range(10):
    distance1 = random.randint(1,10)
    turtle1.forward(distance1)
    distance2 = random.randint(1,10)
    turtle2.forward(distance2)


turtle1.goto(-100,20)
turtle2.goto(-100,-20)

window.exitonclick()

#part B

pygame.init()
window = pygame.display.set_mode()

side_length = 100
xpos = 600 
ypos = 400 

for x in [3,4,6]:
    print(x)

for num_sides in [3,4,6,20,100,360]:
    points = []
    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window,"red",points)
    pygame.display.flip()
    pygame.time.wait(2000)
    window.fill("black")
    pygame.display.flip()
