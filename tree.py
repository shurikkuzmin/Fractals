#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:05:48 2022

@author: shurik
"""
import turtle
screen = turtle.Screen()
screen.setup(1000, 1000)

t = turtle.Turtle()
t.speed("fastest")
#turtle.tracer(False)

def draw_tree(level, branch_size, angle):
    t.forward(branch_size)
    
    if level > 0:
        t.left(angle)
        draw_tree(level - 1, int(branch_size/2), angle)
        t.right(2 * angle)
        draw_tree(level - 1, int(branch_size/2), angle)
        t.left(angle)
    
    t.backward(branch_size)

t.left(90)
draw_tree(5, 200, 30)

turtle.mainloop()    