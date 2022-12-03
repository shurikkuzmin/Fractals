#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 10:27:36 2022

@author: shurik
"""

import turtle

t = turtle.Turtle()
t.speed("fastest")

ratio = 1.3

def flake(level, size):    
    t.forward(0.5*size)
    
    if level > 0:
        t.left(50)
        flake(level-1,int(0.5*size/(ratio + 1)))
        t.right(100)
        flake(level-1,int(0.5*size/(ratio + 1)))
        t.left(50)
    
    t.forward(0.5*size)
    
    if level > 0:
        t.left(50)
        flake(level-1,int(size/(ratio + 1)))
        t.right(50)
        flake(level-1,int(size*ratio/(ratio + 1)))
        t.right(50)
        flake(level-1,int(size/(ratio+1)))
        t.left(50)
    t.backward(size)    
    
t.left(90)

for i in range(6):
    flake(3, 200)
    t.right(60)
    
turtle.mainloop()