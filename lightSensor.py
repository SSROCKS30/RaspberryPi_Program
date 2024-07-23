import os
import datetime
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def RCtimes(RCpins):
    readings = 0
    GPIO.setup(RCpins, GPIO.OUT)
    GPIO.output(RCpins, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(RCpins, GPIO.IN)
    
    # Iterates 1 millisecond over one cycle
    while GPIO.input(RCpins) == GPIO.LOW:
        readings += 1
    
    return readings

while True:
    GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LDRReading = RCtimes(4)
    
    # Print the LDR reading
    print(LDRReading)
    
    # Open a file
    with open("/home/pi/10x10/foo.txt", "a") as fo:  # Open in append mode
        fo.write(GetDateTime + "\n")
        fo.write(str(LDRReading) + "\n")
    
    time.sleep(1)
