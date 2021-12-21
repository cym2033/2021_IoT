import RPi.GPIO as GPIO
import time

LED_PIN1 = 5
LED_PIN2 = 6
LED_PIN3 = 7
SWITCH_PIN1 = 11
SWITCH_PIN2 = 10
SWITCH_PIN3 = 9

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)
GPIO.setup(SWITCH_PIN1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val1 = GPIO.input(SWITCH_PIN1)
        val2 = GPIO.input(SWITCH_PIN2)
        val3 = GPIO.input(SWITCH_PIN3)
        GPIO.output(LED_PIN1,val1)
        GPIO.output(LED_PIN2,val2)
        GPIO.output(LED_PIN3,val3)
        print(val1, val2, val3)
        time.sleep(0.1)


finally:
    GPIO.cleanup()
    print('cleanup and exit')