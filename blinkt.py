#this file contains the code for the onboard LED on the raspberry pi pico W microcontroller, which starts blinking as soon as u run the programm and stops after 3 times.
#Its a little programm I use to see if i pluged in the Pico the right way and its able to receive further commands.

#imports the crucial libraries machine and utime
import machine
import utime

#the onboard LED is stored inside a variable
led = machine.Pin("LED", machine.Pin.OUT)

#i as a counter and the loop that lets the LED blink 
i = 0
while i < 3:
    led.value(1) #value 1 means it receives power and value 0 means no power
    print("LED on") #output in the console so u can see what the Pico should do
    utime.sleep(2) #sleep means that the computer waits (here 2 seconds) before it goes on running the programm
    led.value(0)
    print("LED off")
    utime.sleep(2)
    i = i+1
