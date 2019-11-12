# /usr/bin/env python3
# -*- coding:utf-8 -*-

#
# 02_led_software_pwm.py
#

import sys
import time
import pigpio

LED_PORT = 18
PWM_FREQUENCY = 500             # Hz
RANGE = 100

def main(hostname):
    # Software PWM
    pi = pigpio.pi(hostname)
    pi.set_mode(LED_PORT, pigpio.OUTPUT)
    pi.set_PWM_frequency(LED_PORT, PWM_FREQUENCY)
    pi.set_PWM_range(LED_PORT, RANGE)

    # LEDを2秒間点灯する
    for duty in (5, 20, 50, 80, 100):
        print(duty)
        pi.set_PWM_dutycycle(LED_PORT, duty)
        time.sleep(2)

    # ピンをINPUTモードにしておかないと、LEDが点灯し続けてしまう
    pi.set_mode(LED_PORT, pigpio.INPUT)
    pi.stop()

if __name__ == '__main__':
    hostname = 'localhost'
    if len(sys.argv) > 1:
        hostname = sys.argv[1]

    main(hostname)
