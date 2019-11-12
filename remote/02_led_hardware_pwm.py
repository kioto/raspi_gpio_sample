# /usr/bin/env python3
# -*- coding:utf-8 -*-

#
# 02_led_hardware_pwm.py
#

import sys
import time
import pigpio

LED_PORT = 18
PWM_FREQUENCY = 500             # Hz

def main(hostname):
    # Hardware PWM
    pi = pigpio.pi(hostname)
    pi.set_mode(LED_PORT, pigpio.OUTPUT)
    
    # LEDを2秒間点灯する
    for duty in (5, 20, 50, 80, 100):
        print(duty)
        pi.hardware_PWM(LED_PORT, PWM_FREQUENCY, duty * 10000)
        time.sleep(2)
        
    # ピンをINPUTモードにしておかないと、LEDが点灯し続けてしまう
    pi.set_mode(LED_PORT, pigpio.INPUT)
    pi.stop()


if __name__ == '__main__':
    hostname = 'localhost'
    if len(sys.argv) > 1:
        hostname = sys.argv[1]

    main(hostname)
