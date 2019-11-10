#
# 01_switch_inter.py
#

import RPi.GPIO as GPIO
import time

SWITCH_PORT = 23

GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
GPIO.setup(SWITCH_PORT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cb_switch(ch):
    current_state = GPIO.input(ch)
    if current_state:
        print('OFF')
    else:
        print('Pushed')


GPIO.add_event_detect(SWITCH_PORT, GPIO.BOTH, callback=cb_switch)

time.sleep(10)
