#This file contains the code for my bedarfsampel breadboard circuit.

import machine
import utime


#those are the LEDs for the drivers of the vehicles
red_drivers = machine.Pin(15, machine.Pin.OUT)
yellow_drivers = machine.Pin(14, machine.Pin.OUT)
green_drivers = machine.Pin(13, machine.Pin.OUT)

#these are the LEDs for the people crossing the street
red_people = machine.Pin(12, machine.Pin.OUT)
green_people = machine.Pin(11, machine.Pin.OUT)

#this is the button the people have to press in order to cross the street safely
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_DOWN)



#Next is the infinite loop that waits until the button is pressed which triggers the LEDs changing theyr value
#which gives drivers and persones signals to keep everything save

while True:
    #if no button is pressed people see red and drivers green
    red_people.value(1)
    green_drivers.value(1)
    
    #if the button is pressed it goes through the sequence of changing the LEDs value
    if button.value()== 1:
        utime.sleep(2)
        
        green_drivers.value(0)
        yellow_drivers.value(1)
        utime.sleep(2)
        
        yellow_drivers.value(0)
        red_drivers.value(1)
        utime.sleep(1)
        red_people.value(0)
        green_people.value(1)
        utime.sleep(6)
        
        green_people.value(0)
        utime.sleep(0.3)
        green_people.value(1)
        utime.sleep(0.3)
        green_people.value(0)
        red_people.value(1)
        utime.sleep(1)
        red_drivers.value(0)
        yellow_drivers.value(2)
        utime.sleep(1)
        
        yellow_drivers.value(0)
        green_drivers.value(1)
