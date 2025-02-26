import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

#print(GPIO.input(23), "значение")
while True:
    GPIO.output(3, 0)

GPIO.cleanup()