#All the imports necessary
import utime
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from machine import ADC
from time import sleep


#Now everything for the Display
I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda = machine.Pin(0), scl= machine.Pin(1), freq= 400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)


#Now everything for the sensor
sensor = ADC(4)
conversion_factor = 3.3 / (65535)


#Now we create the while Loop that reads the Temperature every Second calculates it and prints it to the display
while True:
    # Read the sensor as a dicimal number
    value_a = sensor.read_u16()
    # Calculate it into a real number
    spannung = value_a * conversion_factor
    # Turn it into a temperatur
    temperatur = 27 - (spannung - 0.706) / 0.001721
    
    #We have to round the temperatur and then display it
    temperatur = round(temperatur,2)
    string = str(temperatur)
    lcd.move_to(1,0)
    lcd.putstr("Temp: "+string+ "  C")
    
    utime.sleep(2)
