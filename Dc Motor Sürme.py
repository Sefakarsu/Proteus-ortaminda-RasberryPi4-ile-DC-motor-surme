import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

enable_pin = 18
in1_pin = 23
in2_pin = 24

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(in1_pin, GPIO.OUT)
GPIO.setup(in2_pin, GPIO.OUT)

GPIO.output(in1_pin, GPIO.LOW)
GPIO.output(in2_pin, GPIO.HIGH)

pwm = GPIO.PWM(enable_pin, 100)
pwm.start(0)

try:
    while True:
        for i in range(100):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
        for i in range(100, 0, -1):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.02)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()