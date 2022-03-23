import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

try:
    while True:
        val = input()
        if val == 'q':
            break
        try: 
            if float(val) % 1 != 0:
                print("input is not integer")
                continue
            elif int(val) > 255:
                print("num is more than 255")
                continue
            elif int(val) < 0:
                print("num is negative")
                continue
            val = int(val)
            GPIO.output(dac, dec2bin(val))
            print("voltage: ", "{:.4f}".format(3.3 * val / 256), "V")
        except ValueError:
            print("invalid input")
finally: 
    GPIO.output(dac, 0)
    GPIO.cleanup()
