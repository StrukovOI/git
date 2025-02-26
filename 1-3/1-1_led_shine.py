import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)

for i in range(5):

    GPIO.output(20, 1)
    time.sleep(1)
    
    GPIO.output(20, 0)
    time.sleep(1)
