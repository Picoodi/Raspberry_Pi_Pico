from machine import ADC
from time import sleep
import utime

# Initialising des ADC4 Pins for the Sensor and create the Pins for the 7Segment displays as well as the Pins for the LEDs.
sensor = ADC(4)
conversion_factor = 3.3 / (65535)


#Led Pins
BlueLed = machine.Pin(0, machine.Pin.OUT)
tenled = machine.Pin(3, machine.Pin.OUT)
twentyled = machine.Pin(2, machine.Pin.OUT)
thirtyled = machine.Pin(1, machine.Pin.OUT)


#7Segment Display Pins
top = machine.Pin(17, machine.Pin.OUT)
topright = machine.Pin(16, machine.Pin.OUT)
bottomright = machine.Pin(13, machine.Pin.OUT)
bottom = machine.Pin(14, machine.Pin.OUT)
bottomleft = machine.Pin(15, machine.Pin.OUT)
topleft = machine.Pin(18, machine.Pin.OUT)
middle = machine.Pin(19, machine.Pin.OUT)
dot = machine.Pin(12, machine.Pin.OUT)


#we create a funtion for displayig the numbers on the display more easily 
def display():
    print(temperatur)
    
    #set every walue to 0 so its a fresh start everytime we plug the pico in
    top.value(0)
    topright.value(0)
    bottomright.value(0)
    bottom.value(0)
    bottomleft.value(0)
    topleft.value(0)
    middle.value(0)
    dot.value(0)
    
    if temperatur == 0:
        top.value(1)
        topright.value(1)
        topleft.value(1)
        bottom.value(1)
        bottomright.value(1)
        bottomleft.value(1)
        
    if temperatur == 1:
        topright.value(1)
        bottomright.value(1)
        
    if temperatur == 2:
        top.value(1)
        bottom.value(1)
        topright.value(1)
        bottomleft.value(1)
        middle.value(1)
        
    if temperatur == 3:
        top.value(1)
        bottom.value(1)
        middle.value(1)
        topright.value(1)
        bottomright.value(1)
        
    if temperatur == 4:
        topright.value(1)
        topleft.value(1)
        middle.value(1)
        bottomright.value(1)
        
    if temperatur == 5:
        top.value(1)
        middle.value(1)
        bottom.value(1)
        topleft.value(1)
        bottomright.value(1)
        
    if temperatur == 6:
        dot.value(1)
        top.value(1)
        topleft.value(1)
        middle.value(1)
        bottomleft.value(1)
        bottomright.value(1)
        bottom.value(1)
        
    if temperatur == 7:
        top.value(1)
        topright.value(1)
        bottomright.value(1)
        
    if temperatur == 8:
        top.value(1)
        bottom.value(1)
        middle.value(1)
        topright.value(1)
        topleft.value(1)
        bottomleft.value(1)
        bottomright.value(1)
        
    if temperatur == 9:
        dot.value(1)
        top.value(1)
        topright.value(1)
        topleft.value(1)
        middle.value(1)
        bottomright.value(1)
        bottom.value(1)


#set every walue to 0 so its a fresh start everytime we plug the pico in
BlueLed.value(0)
tenled.value(0)
twentyled.value(0)
thirtyled.value(0)
top.value(0)
topright.value(0)
bottomright.value(0)
bottom.value(0)
bottomleft.value(0)
topleft.value(0)
middle.value(0)
dot.value(0)


# Infinite Loop so it works
while True:    
    
    # Read the sensor as a dicimal number
    value_a = sensor.read_u16()
    # Calculate it into a real number
    spannung = value_a * conversion_factor
    # Turn it into a temperatur
    temperatur = 27 - (spannung - 0.706) / 0.001721
    
    #We have to round the temperatur cause we only use on display
    temperatur = round(temperatur,0)
    

    #we look if the temperatur is negativ so we activate the blue LED and calculate it times -1
    if temperatur < 0:
        BlueLed.value(1)
        temperatur = temperatur * -1
        
    if temperatur >= 10 and temperatur < 20:
        tenled.value(1)
        twentyled.value(0)
        thirtyled.value(0)
        temperatur = temperatur -10
        display()
        
    if temperatur >= 20 and temperatur < 30:
        tenled.value(1)
        twentyled.value(1)
        thirtyled.value(0)
        temperatur = temperatur -20
        display()
        
    if temperatur >= 30:
        tenled.value(1)
        twentyled.value(1)
        thirtyled.value(1)
        temperatur = temperatur -30
        display()
        
        
    utime.sleep(2)
