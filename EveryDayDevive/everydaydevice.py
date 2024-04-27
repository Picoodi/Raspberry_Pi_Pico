#necessary imports
import utime
from machine import I2C, Pin, ADC

#drivers for I2C Display
from lcd_api import LcdApi     
from pico_i2c_lcd import I2cLcd

#creating the Display
I2C_ADDR = 39          
I2C_NUM_ROWS = 2       
I2C_NUM_COLS = 16      
i2c = I2C(0, sda = machine.Pin(0), scl= machine.Pin(1), freq= 400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Initialising the ADC4 Temperature Sensor
temp_sensor = ADC(4)
conversion_factor = 3.3 / (65535)

#implementing all the buttons
start_button = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_DOWN)
pause_button = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
settings_button = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)

hour_button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
minutes_button = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_DOWN)
seconds_button = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_DOWN)




# a settings function that lets u change the time   
def settings(h, m, s):
    timelist = [] #a list that gets returned
    
    while settings_button.value() == 0:
        #looking that the time isnt getting greater then necessary
        if s > 59:
            s = 0
        
        if m > 59:
            m = 0
            
        if h > 23:
            h = 0
                

        #time buttons are getting checked if they are pressed or not and change the data if necessary
        if hour_button.value() == 1:
            h = h +1
        if minutes_button.value() == 1:
            m = m +1
        if seconds_button.value() == 1:
            s = s +1
        
        lcd.move_to(0,0)
        he = str(h)
        me = str(m)
        se = str(s)
        lcd.clear()
        lcd.putstr(he + ":" + me + ":" + se)
        utime.sleep(0.2)
        
    #if the settings button got pressed again it returns the list 
    else:
        hor = int(h)
        mi = int(m)
        se = int(s)
        timelist.append(hor)
        timelist.append(mi)
        timelist.append(se)
        return timelist
    
    
  
  
  
  
# starting variables when the device gets booted
hours = 0
minutes = 0
seconds = 0
timer_running = False
    
    
while True:
    #time settings button
    if settings_button.value() == 1:
        utime.sleep(1)
        result = settings(hours, minutes, seconds)
        hours = result[0]
        minutes = result[1]
        seconds = result[2]
    
    
    
    #time that gets read and wrote to the Display
    if seconds >= 60:
        seconds = 0
        minutes = minutes+1
        
    if minutes >= 60:
            minutes = 0
            hours = hours+1
            
    if hours >= 24:
                hours = 0
    
    hour = str(hours)
    minute = str(minutes)
    second = str(seconds)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr(hour + ":" + minute + ":" + second)
    

    #temperatur that gets read and wrote to the display
    value_a = temp_sensor.read_u16()
    spannung = value_a * conversion_factor
    temperatur = 27 - (spannung - 0.706) / 0.001721
    temperatur = round(temperatur,1)
    string = str(temperatur)
    lcd.move_to(10,0)
    lcd.putstr(string+ " C")
    
    
    #end of one loop go through that increases the time by one second by sleeping for one second
    seconds = seconds +1
    utime.sleep(1)
