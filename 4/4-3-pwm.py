import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

p=GPIO.PWM(24, 100)
p.start(0)
try:
    while True:
        a=float(input('Введите коэффициент заполнения\n'))
        p.start(a)
except ArithmeticError:
    a=None
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()
