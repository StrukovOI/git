import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(leds, GPIO.OUT)

for i in range(3):
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

GPIO.cleanup()
