# /usr/bin/env python3
# -*- coding:utf-8 -*-

#
# 02_led_haedware_pwm_test.py
#

import sys
import time
import pigpio

LED_PORT = 18

def main(hostname, freq, duty):
    # Software PWM
    pi = pigpio.pi(hostname)
    pi.set_mode(LED_PORT, pigpio.OUTPUT)

    try:
        pi.hardware_PWM(LED_PORT, freq, duty * 10000)
        time.sleep(60)

    except KeyboardInterrupt:
        pass

    # ピンをINPUTモードにしておかないと、LEDが点灯し続けてしまう
    pi.set_mode(LED_PORT, pigpio.INPUT)
    pi.stop()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python %s <<frequency> <duty_cycle> [<hostname>]'
              % sys.argv[0])
        exit()

    hostname = 'localhost'
    if len(sys.argv) >= 4:
        hostname = sys.argv[3]

    main(int(sys.argv[1]), int(sys.argv[2]), hostname)
