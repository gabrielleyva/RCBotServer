import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

class Servo():


    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.__pwm = GPIO.PWM(18, 100)
        duty = float(10) / 10.0 + 2.5
        self.__pwm.start(3.5)
    
    def turn(self, value):
        #self.__pwm.start(5)
        duty = float(value) / 10.0 + 2.5
        self.__pwm.ChangeDutyCycle(duty)
