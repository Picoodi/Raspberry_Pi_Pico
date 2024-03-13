# Bibliotheken laden
from machine import ADC
from time import sleep

# Initialisierung des ADC4
sensor = ADC(4)
conversion_factor = 3.3 / (65535)

# Wiederholung einleiten (Schleife)
while True:
    # Temparatur-Sensor als Dezimalzahl lesen
    value_a = sensor.read_u16()
    # Dezimalzahl in eine reele Zahl umrechnen
    spannung = value_a * conversion_factor
    # Spannung in Temperatur umrechnen
    temperatur = 27 - (spannung - 0.706) / 0.001721
    # Ausgabe in der Kommandozeile/Shell
    print("Dezimalzahl: ", value_a)
    print("Spannung (V): ", spannung)
    print("Temperatur (°C): ", temperatur)
    print()
    # 2 Sekunden warten
    sleep(3)
