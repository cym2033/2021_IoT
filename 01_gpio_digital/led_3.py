import RPi.GPIO as GPIO
import time

RED = 5
YELLOW = 6
GREEN = 7
GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

GPIO.output(RED, GPIO.HIGH)
time.sleep(2)
GPIO.output(RED, GPIO.LOW)
GPIO.output(YELLOW, GPIO.HIGH)
time.sleep(2)
GPIO.output(YELLOW, GPIO.LOW)
GPIO.output(GREEN, GPIO.HIGH)
time.sleep(2)
GPIO.output(GREEN, GPIO.LOW)