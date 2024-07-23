import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT) # LED RED
GPIO.setup(23, GPIO.OUT) # LED BLUE

os.system('clear')

print("Which LED would you like to blink?")
print("1: Red")
print("2: Blue")

led_choice = input("Choose your option: ")
count = input("How many times would you like to blink the LED? ")

if led_choice == '1':
    for i in range(int(count)):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
elif led_choice == '2':
    for i in range(int(count)):
        GPIO.output(23, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(23, GPIO.LOW)
        time.sleep(1)
else:
    print("Invalid option")
    
