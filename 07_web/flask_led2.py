from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN = 5

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

@app.route("/")
def hello():
    return render_template("led.html")

@app.route("/led/<color>/<op>")
def led_op(color, op):
    if op == "on" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.HIGH)
        return 'RED LED ON'

    if op == "off" and color == "red":
        GPIO.output(RED_LED_PIN, GPIO.LOW)
        return 'RED LED OFF'

    if color == "blue" and op == "on":
        GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
        return 'BLUE LED ON'

    if color == "blue" and op == "off":
        GPIO.output(BLUE_LED_PIN, GPIO.LOW)
        return 'BLUE LED OFF'

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()