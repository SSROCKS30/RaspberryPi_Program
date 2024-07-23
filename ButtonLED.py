import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.IN) # Button
GPIO.setup(18, GPIO.OUT) # LED

os.system('clear')
print("Button + GPIO")

while True:
    if(GPIO.input(10) == 1):
        GPIO.output(18, GPIO.HIGH)
        print("LED ON")
        os.system('date')
        time.sleep(5)
    else:
        GPIO.output(18, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)
        os.system('clear')

