import turtle
import random

PEN = turtle.Turtle()
WINDOW = turtle.Screen()
WIDTH = WINDOW.window_width()//2
HEIGHT = WINDOW.window_height()//2
WINDOW.bgcolor("black")

def main():
    stars = int(input("How many stars would you like to draw? ")) 
    message = print("Pick a color for your stars")
    message = print("0 is blue, 1 is green, 2 is yellow, 3 is red, 4 is pink, 5 is a random color")
    choice = int(input("What color would you like: "))
    PEN.pencolor(star_color(choice))
    num_of_stars(stars)
    PEN.pendown()
    WINDOW.exitonclick()

def star_color(choice):
    color_list = ["blue","green","yellow","red","pink"]
    if choice < 5:
        color = color_list[choice]
    elif choice == 5:
        color = random.choice(color_list)
    else:
        while choice > 5:
            choice = int(input("pick a smaller numer: "))
        color = color_list[choice]
    return color


def num_of_stars(num):
    for i in range(num):
        PEN.penup()
        xcor = random.randint(WIDTH*-1,WIDTH)
        ycor = random.randint(HEIGHT*-1,HEIGHT)
        PEN.goto(xcor,ycor)
        PEN.pendown()
        PEN.left(55)
        PEN.forward(25)
        for i in range(4):
            PEN.left(145)
            PEN.forward(25)

main()



