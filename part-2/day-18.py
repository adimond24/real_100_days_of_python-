import turtle as t
import heros
import villians
import random

tim = t.Turtle()
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(colors())
        tim.circle(100)
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colored = (r, g, b)
    return colored
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)

# for i in range(100):
#     steps = int(random() * 100)
#     angle = int(random()*360)
#
#     t.right(angle)
#     t.color(random.choice(color))
#     t.fd(steps)
#
# directions = [0, 90, 180, 270]
# tim.pensize(30)
# tim.speed("fastest")
#
# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))







# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color('orange')
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
#
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
#
#
#
#
#
#
screen = t.Screen()
screen.exitonclick()

# from turtle import *
# from random import *
#
# choice([1, 2, 3])
