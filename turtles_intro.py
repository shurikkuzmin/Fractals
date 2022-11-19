#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 10:24:02 2022

@author: shurik
"""
import turtle

t = turtle.Turtle()

t.forward(100)
t.circle(50)
t.left(45)
t.forward(50)
t.goto(200,200)

#t.begin_poly()
t.begin_fill()
t.left(50)
t.forward(40)
t.left(50)
t.forward(40)
t.end_fill()
#t.end_poly()

turtle.mainloop()
