from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 4

try:
    print("Waiting to display")
    while True:
        now = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string(f"{temperature}*C {humidity}%",2)
        time.sleep(1)

finally:
    print("Cleaning Up!")
    display.lcd_clear()