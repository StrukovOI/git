import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

def dec(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


def adc():
    a=0
    for i in range(8):
        a+=2**(7-i)
        GPIO.output(dac, dec(a))
        time.sleep(0.001)
        if GPIO.input(comp)==0:
            a-=2**(7-i)
    return a

try:
    GPIO.output(troyka, GPIO.HIGH)
    while True:
        b=adc()
        volt = b / 256 * 3.3
        print("Цифровое значение: {:3d}, Напряжение: {:.2f}В".format(b, volt))
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Программа остановлена')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()