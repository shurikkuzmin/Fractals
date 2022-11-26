#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:02:56 2022

@author: shurik
"""

import turtle
import numpy

t = turtle.Turtle()
t.speed("fastest")
screen = turtle.Screen()
screen.setup(1600, 1200)

def line(level, size):
    if level == 0:
        t.forward(size)
        return
    line(level - 1, int(size / 3))
    t.left(45)
    line(level - 1, int(size / 3))
    t.right(90)
    line(level - 1, int(size / 3))
    t.left(45)
    line(level - 1, int(size / 3))

main_size = 400
t.penup()
t.goto(-int(main_size/2),int(main_size/2*numpy.sqrt(3.0)))
t.pendown()

for i in range(6):
    line(4, main_size)
    t.right(60)

turtle.mainloop()