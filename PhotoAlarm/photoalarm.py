
import machine
import utime

PhotoResistor = machine.ADC(1)
buzzer = machine.Pin(15, machine.Pin.OUT)


while True:
    Bright_Level = PhotoResistor.read_u16()
    print(Bright_Level)
    
    if Bright_Level > 55000:
        utime.sleep(1.5)
        buzzer.value(1)
        utime.sleep(1)
        buzzer.value(0)
    elif Bright_Level < 55000:
        buzzer.value(0)
        
    utime.sleep(0.1)
