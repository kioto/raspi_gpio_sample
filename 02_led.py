#
# 02_led.py
#

import RPi.GPIO as GPIO
import time

LED_PORT = 18

GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
GPIO.setup(LED_PORT, GPIO.OUT)

# LEDを5秒間点灯する
GPIO.output(LED_PORT, True)
time.sleep(5)
GPIO.output(LED_PORT, False)

GPIO.cleanup()

print('done')
