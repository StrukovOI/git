import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

def nd(value):
    signal=dec(value)
    GPIO.output(dac, signal)

def adc():
    val=0
    for i in range(8):
        bv=1<<(7-i)
        val+=bv
        GPIO.output(dac, dec(val))
        time.sleep(0.001)
        if GPIO.input(comp)==0:
            val-=bv
    return val


try:
    while True:
        dv=adc()
        volt = dv / 256 * 3.3
        print("Цифровое значение: {:3d}, Напряжение: {:.2f}В".format(dv, volt))
       
except KeyboardInterrupt:
    print('Программа остановлена')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()