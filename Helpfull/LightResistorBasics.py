import machine
import utime

#an ADC Pin is required for the resistor 
PhotoResistor = machine.ADC(1) 
LED = machine.Pin(15, machine.Pin.OUT)


LED.value(1) 
while True:
    Bright_Level = PhotoResistor.read_u16()
    
    print(Bright_Level)
    utime.sleep(0.1)
