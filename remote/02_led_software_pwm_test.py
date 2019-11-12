# /usr/bin/env python3
# -*- coding:utf-8 -*-

#
# 02_led_software_pwm_test.py
#

import sys
import time
import pigpio

LED_PORT = 18
RANGE = 100

def main(freq, duty, hostname):
    # Software PWM
    pi = pigpio.pi(hostname)
    pi.set_mode(LED_PORT, pigpio.OUTPUT)
    pi.set_PWM_frequency(LED_PORT, freq)
    pi.set_PWM_range(LED_PORT, RANGE)

    try:
        pi.set_PWM_dutycycle(LED_PORT, duty)
        time.sleep(60)

    except KeyboardInterrupt:
        pass

    # ピンをINPUTモードにしておかないと、LEDが点灯し続けてしまう
    pi.set_mode(LED_PORT, pigpio.INPUT)
    pi.stop()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python %s <frequency> <duty_cycle> [<hostname>]'
              % sys.argv[0])
        exit()
    hostname = 'localhost'
    if len(sys.argv) >= 4:
        hostname = sys.argv[3]

    main(int(sys.argv[1]), float(sys.argv[2]), hostname)
