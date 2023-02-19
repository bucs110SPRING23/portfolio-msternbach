import turtle

sides = int(input("Enter number of sides: "))
length = int(input("Enter length of sides: "))

pen = turtle.Turtle()
pen.color("orange")

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)

window.exitonclick()