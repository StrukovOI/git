import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    a=float(input('Введите значение периода сигнала\n'))/256
    b=0
    while True:
        while b<=254:
            GPIO.output(dac, dec(b))
            b+=1
            time.sleep(a)
        while b>=1:
            GPIO.output(dac, dec(b))
            b-=1

except ArithmeticError:
    a=None
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()