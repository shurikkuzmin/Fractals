#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 10:05:48 2022

@author: shurik
"""
import turtle

t = turtle.Turtle()

def draw_tree(level, branch_size, angle):
    if level == 0:
        t.forward(branch_size)
        t.left(180)
        t.forward(branch_size)
        t.left(180)
        return 
        
    t.forward(branch_size)
    t.left(angle)
    draw_tree(level - 1, int(branch_size/2), angle)
    t.right(2 * angle)
    draw_tree(level - 1, int(branch_size/2), angle)
    t.left(angle)
    t.backward(branch_size)

t.left(90)
draw_tree(5, 200, 30)

turtle.mainloop()    