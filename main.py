# #extract color from an image
# import colorgram
#
# rgb_colors=[]
# colors = colorgram.extract('hirst.jpg', 10)
#
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random

color = [(242, 243, 248), (211, 165, 8), (247, 232, 242), (63, 113, 157), (107, 155, 205), (244, 236, 222), (220, 167, 97), (48, 128, 94), (202, 124, 170), (57, 176, 140)]

tim = turtle.Turtle()
#get him to move the ten pace, then start over on next row
screen=Screen()
xpos =tim.xcor()
ypos = tim.ycor()
screen.colormode(255)
tim.width()
tim.speed('fastest')
def stamp_and_move():
    tim.dot(15, random.choice(color))
    tim.penup()
    tim.forward(50)

def line_up():
    new_y=ypos+50.0
    new_x=xpos
    tim.goto(new_x,new_y)

for _ in range(10):
    for _ in range(10):
        stamp_and_move()
    line_up()
    ypos += 50.0

#get it to be a dot

#get it to change colors using RGB values extracted form Hirst





screen.exitonclick()


