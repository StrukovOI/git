import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT)

def dec(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]



def adc():
    value=0
    for i in range(8):
        value+=2**(7-i)
        GPIO.output(dac, dec(value))
        time.sleep(0.001)
        if GPIO.input(comp)==1:
            value-=(2**(7-i))
    return value

try:
    while True:
        dv=adc()

        volt = dv / 256 * 3.3
        if dv<28:
            GPIO.output(leds, [0]*8)
        elif dv<57:
            GPIO.output(leds, [0, 0, 0, 0, 0, 0, 0, 1])
        elif dv<85:
            GPIO.output(leds, [0, 0, 0, 0, 0, 0, 1, 1])
        elif dv<114:
            GPIO.output(leds, [0, 0, 0, 0, 0, 1, 1, 1])
        elif dv<142:
            GPIO.output(leds, [0, 0, 0, 0, 1, 1, 1, 1])
        elif dv<171:
            GPIO.output(leds, [0, 0, 0, 1, 1, 1, 1, 1])
        elif dv<199:
            GPIO.output(leds, [0, 0, 1, 1, 1, 1, 1, 1])
        elif dv<228:
            GPIO.output(leds, [0, 1, 1, 1, 1, 1, 1, 1])
        else:
            GPIO.output(leds, [1, 1, 1, 1, 1, 1, 1, 1])
        print("Цифровое значение: {:3d}, Напряжение: {:.2f}В".format(dv, volt))

except KeyboardInterrupt:
    print('Программа остановлена')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()