import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins
GPIO.setup(23, GPIO.IN)    # PIR sensor
GPIO.setup(24, GPIO.OUT)   # Buzzer

try:
    time.sleep(2)  # Stabilize the sensor

    while True:
        if GPIO.input(23):  # If motion is detected by the PIR sensor
            GPIO.output(24, True)  # Turn on the buzzer
            time.sleep(0.5)  # Buzzer stays on for 0.5 seconds
            GPIO.output(24, False)  # Turn off the buzzer
            print("Motion Detected...")
            time.sleep(5)  # Avoid multiple detections

        time.sleep(0.1)  # Loop delay, should be less than detection delay

except KeyboardInterrupt:
    print("Program terminated")

finally:
    GPIO.cleanup()  # Clean up GPIO settings
