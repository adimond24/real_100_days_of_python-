import colorgram
import turtle as turtle_module
import random
turtle_module.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

rgb_colors = []
colors = colorgram.extract('painting.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
color_list = [rgb_colors]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
