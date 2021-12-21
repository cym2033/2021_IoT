import RPi.GPIO as GPIO
import time

piezo_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezo_PIN, GPIO.OUT)

pwm = GPIO.PWM(piezo_PIN, 1)
pwm.start(10)

melody = [1, 62, 294, 330, 349, 392, 440, 494, 523]
music = [5, 5, 6, 6, 5, 5, 3, 5, 5, 3, 3, 2, 5, 5, 6, 6, 5, 5, 3, 5, 3, 2, 3, 1]

try:
    for i in music:
        pwm.ChangeFrequency(melody[i])
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanip()