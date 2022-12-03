#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:22:01 2022

@author: shurik
"""

import turtle

t = turtle.Turtle()
t.speed("fastest")

num_circles = 5

def circus(level, radius):
    t.circle(radius)
    if level > 0:
        for i in range(num_circles):
            circus(level-1,int(radius/4))
            t.penup()
            t.circle(radius,extent=int(360 / num_circles))
            t.pendown()

circus(3, 250)

turtle.mainloop()