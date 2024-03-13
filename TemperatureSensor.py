# Bibliotheken laden
from machine import ADC
from time import sleep

# Initialising des ADC4 Pins for the Sensor and create the Pins for the 7Segment displays as well as the Pins for the LEDs.
sensor = ADC(4)
conversion_factor = 3.3 / (65535)

a = machine.Pin(, machine.Pin.OUT)
b = machine.Pin(, machine.Pin.OUT)
c = machine.Pin(, machine.Pin.OUT)
d = machine.Pin(, machine.Pin.OUT)
e = machine.Pin(, machine.Pin.OUT)
f = machine.Pin(, machine.Pin.OUT)
g = machine.Pin(, machine.Pin.OUT)
dp = machine.Pin(, machine.Pin.OUT)


# Infinite Loop so it works
while True:
    # Read the sensor as a dicimal number
    value_a = sensor.read_u16()
    # Calculate it into a real number
    spannung = value_a * conversion_factor
    # Turn it into a temperatur
    temperatur = 27 - (spannung - 0.706) / 0.001721

    #we look if the 

    #we need to know if the temperatur is only 1 or 2 digit
    if temperatur < 10:



    
    # little 1 second buffer 
    sleep(1)
