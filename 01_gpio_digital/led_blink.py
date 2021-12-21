import RPi.GPIO as GPIO
import time

RED = 9
YELLOW = 8
GREEN = 7
GPIO.setmode(GPIO.BCM) #BCM pin번호를 따르겠다는 의미
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

for i in range(1, 11):
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("led on")
    time.sleep(0.05*i)
    GPIO.output(LED_PIN, GPIO.LOW)
    print("led off")
    time.sleep(0.05*i)

GPIO.cleanup() #pin 초기화