import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT, initial = 0)
GPIO.setup(22, GPIO.OUT)

gp = GPIO.PWM(22, 100)
gp.start(0)

try:
    while True:
        print("cycle: ")
        duty = float(input())
        gp.start(duty)
        print(str(3.3 * duty / 100) + "V")
finally:
    GPIO.cleanup()
