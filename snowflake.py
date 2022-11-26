#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:27:36 2022

@author: shurik
"""

import turtle

t = turtle.Turtle()

def flake(level, size):    
    t.forward(size)
    if level > 0:
        t.left(30)
        flake(level-1,int(size/2.5))
        t.right(30)
        t.forward(int(size*1.5))
        t.backward(int(size*1.5))
        t.right(30)
        t.forward(size)
        t.backward(size)
        t.left(30)
    t.backward(size)    
    
t.left(90)

for i in range(6):
    flake(4, 200)
    t.right(60)
    
turtle.mainloop()