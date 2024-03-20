from machine import ADC
from time import sleep

# Initialising the ADC4
sensor = ADC(4)
conversion_factor = 3.3 / (65535)


while True:
    # Temparatur-Sensor as Decimal
    value_a = sensor.read_u16()
    # Decimal into real number
    spannung = value_a * conversion_factor
    # Voltage in Temperatur
    temperatur = 27 - (spannung - 0.706) / 0.001721
    # Show it in the Terminal window
    print("Dezimalzahl: ", value_a)
    print("Spannung (V): ", spannung)
    print("Temperatur (°C): ", temperatur)
    print()
    # 2 Sekunden warten
    sleep(3)
