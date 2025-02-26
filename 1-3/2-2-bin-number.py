import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
number=[]
dac = [6, 12, 5, 0, 1, 7, 11, 8]

for i in range(8):
    number.append(random.randint(0, 1))
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(5)
GPIO.output(dac, 0)
GPIO.cleanup()

number = [0, 0, 0, 0, 0, 1, 0, 0]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.output(dac, number)
time.sleep(10)


GPIO.cleanup()