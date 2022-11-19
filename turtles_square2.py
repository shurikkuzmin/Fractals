#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 09:58:19 2022

@author: shurik
"""
import turtle

t = turtle.Turtle()

def square(size, counter):
    t.penup()
    for i in range(2):
        t.forward(int(size / 2))
        t.left(90)
    
    t.pendown()
    if counter % 2 == 0:
        t.fillcolor("pink")
    else:
        t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(0,0)
    t.left(180)
    t.pendown()

for i in range(10):
    square(200, i)
    t.left(24)

turtle.mainloop()


