#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 09:58:19 2022

@author: shurik
"""
import turtle

t = turtle.Turtle()

def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)
        

for i in range(30):
    square(100)
    t.penup()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.left(60)
    t.pendown()

turtle.mainloop()


