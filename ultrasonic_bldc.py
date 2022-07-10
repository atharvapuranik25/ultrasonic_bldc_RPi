import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

TRIG=40
ECHO=38

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

b = GPIO.PWM(7, 50)

b.start(0)
print ("starting 0")
time.sleep(3)

b.ChangeDutyCycle(3)
print("start")
time.sleep(3)

print("distance measurement in progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print("waiting for sensor to settle")
time.sleep(0.2)

i=5

while i<8:
	print(i)
	b.ChangeDutyCycle(i)
	time.sleep(.25)
	i +=.02

while True:
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:",distance,"cm")
    if distance>50:
        b.ChangeDutyCycle(6)
    else:
        b.ChangeDutyCycle(8)
    time.sleep(1)  