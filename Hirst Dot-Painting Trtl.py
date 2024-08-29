import turtle
from turtle import *
import colorgram as cg
import random


tintin = Turtle()
tintin.shape()
turtle.colormode(255)
tintin.color("#9932cc")

my_colors = []
extr_colors = cg.extract("hirst_dot.jpg", 20)

for i in extr_colors:
    grad = i.rgb
    tup = (grad.r, grad.g, grad.b)
    my_colors.append(tup)


color_lst = ["DarkOrchid", "DarkSlateBlue", "DarkSlateGrey", "Coral4", "Coral1", "DarkOliveGreen4",
            "LightSalmon4", "DarkSalmon", "IndianRed", "Ivory4", "LightPink4", "LightBlue", "LightBlue4",
            "MediumPurple", "LightSlateBlue", 'Peru', "brown4"]


def dot_paint(n):
    for a in range(n):
        for b in range(n):
            tintin.speed("fastest")
            tintin.dot(20, random.choice(color_lst))
            tintin.penup()
            tintin.forward(40)
            tintin.pendown()
        if a % 2 == 0:
            tintin.speed("fastest")
            tintin.right(90)
            tintin.dot(20, random.choice(color_lst))
            tintin.penup()
            tintin.forward(40)
            tintin.pendown()
            tintin.right(90)
        else:
            tintin.speed("fastest")
            tintin.left(90)
            tintin.dot(20, random.choice(color_lst))
            tintin.penup()
            tintin.forward(40)
            tintin.pendown()
            tintin.left(90)


dot_paint(10)


my_screen = Screen()
my_screen.exitonclick()


