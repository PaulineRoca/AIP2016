# -*- coding: utf-8 -*- -
import turtle
def polygon(n):
    """ dessine un polygone à n côtés"""
    for _ in range(n):
        turtle.forward(100)
        turtle.left(360/n)
    turtle.mainloop()

polygon(7)
