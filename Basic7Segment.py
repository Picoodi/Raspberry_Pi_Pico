#This file contains th code for my Basic 7Segment Display which counts to 9 with the help of a Button and as soon as it reaches 10 it starts again from 0.

from machine import Pin
import utime

middle = machine.Pin(, machine.Pin.OUT)
topleft = machine.Pin(, machine.Pin.OUT)
top = machine.Pin(, machine.Pin.OUT)
topright = machine.Pin(, machine.Pin.OUT)
dot = machine.Pin(, machine.Pin.OUT)
bottomright= machine.Pin(, machine.Pin.OUT)
bottom = machine.Pin(, machine.Pin.OUT)
bottomleft = machine.Pin(, machine.Pin.OUT)



i = 0
while True:
    top.value(0)
    bottom.value(0)
    middle.value(0)
    topright.value(0)
    topleft.value(0)
    bottomleft.value(0)
    bottomright.value(0)

    if i == 0:
        top.value(1)
        topright.value(1)
        topleft.value(1)
        bottom.value(1)
        bottomright.value(1)
        bottomleft.value(1)
        
        
    if i == 1:
        topright.value(1)
        bottomright.value(1)
        
    if i == 2:
        top.value(1)
        bottom.value(1)
        topright.value(1)
        bottomleft.value(1)
        middle.value(1)
        
    if i == 3:
        top.value(1)
        bottom.value(1)
        middle.value(1)
        topright.value(1)
        bottomright.value(1)
        
    if i == 4:
        topright.value(1)
        topleft.value(1)
        middle.value(1)
        bottomright.value(1)
        
    if i == 5:
        top.value(1)
        middle.value(1)
        bottom.value(1)
        topleft.value(1)
        bottomright.value(1)
        
    if i == 6:
        dot.value(1)
        top.value(1)
        topleft.value(1)
        middle.value(1)
        bottomleft.value(1)
        bottomright.value(1)
        bottom.value(1)
        
    if i == 7:
        top.value(1)
        topright.value(1)
        bottomright.value(1)
        
    if i == 8:
        top.value(1)
        bottom.value(1)
        middle.value(1)
        topright.value(1)
        topleft.value(1)
        bottomleft.value(1)
        bottomright.value(1)
        
    if i == 9:
        dot.value(1)
        top.value(1)
        topright.value(1)
        topleft.value(1)
        middle.value(1)
        bottomright.value(1)
        bottom.value(1)
        
    if i == 10:
        i = 0
