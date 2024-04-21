import utime
from machine import I2C, Pin  

#next the 2 other filed including the drivers are getting importet those are the other 2 files 
#you can find in my repos. They have to be installed onto the pi
from lcd_api import LcdApi     
from pico_i2c_lcd import I2cLcd



I2C_ADDR = 39          #here we include the address of the display in this case 39
I2C_NUM_ROWS = 2       #here the amount of rows of the display has
I2C_NUM_COLS = 16      #and here the ammount of coloums in a row

#next we create the actuall display
i2c = I2C(0, sda = machine.Pin(0), scl= machine.Pin(1), freq= 400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#and here a basic script to write hello in the first and world in the second coloum
lcd.clear()
lcd.putstr("Hello")
lcd.move_to(5,1)
lcd.putstr("World")
utime.sleep(10)
lcd.clear()
