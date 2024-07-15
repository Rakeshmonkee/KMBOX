#Made with <3 by RakeshMonkee

import serial
from time import sleep
import random

while True:
    COM = input("Enter COM Number: ")
    try:
        COM = int(COM)
        break
    except ValueError:
        print("Please Enter A Valid Number")


ser = serial.Serial(f'COM{COM}',115200)

if not ser.isOpen():
    ser.open()

z = 10

for i in range(z) :
    x = random.randint(-25,25)
    y = random.randint(-25,25)

    ser.write(f'km.move({x},{y})\r\n'.encode('utf-8'))

    sleep(1)

