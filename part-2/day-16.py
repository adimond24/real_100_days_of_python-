# from turtle import Turtle, Screen
from numpy.ma.core import right_shift
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cyan1")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick(
#

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electic", "fire", "water"])
table.align = "l"
print(table)

