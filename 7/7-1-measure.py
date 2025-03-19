import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

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
    return round(value*0.012890625, 4)


def bin_leds():
    
        dv=adc()*256
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


def measure():
    meas=[]
    GPIO.output(troyka, GPIO.HIGH)
    start=time.time()
    while adc()!=2.475:
        meas.append(adc())
        bin_leds()
        print(meas)
    meas.append(adc())
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    while adc()>0.06445:
        meas.append(adc())
        bin_leds()
        print(meas)
    meas.append(adc())
    end=time.time()
    GPIO.cleanup()
    zeit=end-start
    return meas, zeit
    
try:
    meas, zeit = measure()
    plt.plot(meas)
    plt.show()

    with open('data.txt', 'w') as f:
        for i in meas:
            f.write(f"{str(i)}\n")

    print(f'Общая продолжительность эксперимента - {round(zeit, 4)} c, \nпериод одного измерения - {round(zeit/len(meas), 5)} c,\nсредняя частота дискретизации проведённых измерений - {round(1/zeit*len(meas), 3)} Гц\nшаг квантования АЦП - {round(3.3/256, 5)} В')
except KeyboardInterrupt:
    print('Программа остановлена')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()
