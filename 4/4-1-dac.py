import RPi.GPIO as GPIO
#import math
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def dec(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    while True:
        a=input('Введите целое число от 0 до 255\n')
        if a=='q':
            break
        try:
            value=int(a)
            if value<0:
                print('Введено отрицательное число')
                continue
            elif value>255:
                print('Введено значение, превышающее возможности 8-разрядного ЦАП')
                continue

            b=dec(int(a))
            GPIO.output(dac, b)
            print('Напряжение ', int(a)/255*3.3, ' В')
        except ValueError:
            print('Введено не числовое значение или не целое число')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
