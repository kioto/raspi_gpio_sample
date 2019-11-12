#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import pigpio

LED_PORT = 18
HIGH = 1
LOW = 0

def main(hostname):
    pi = pigpio.pi(hostname)
    pi.set_mode(LED_PORT, pigpio.OUTPUT)

    # LEDを5秒間点灯する
    pi.write(LED_PORT, HIGH)
    time.sleep(5)
    pi.write(LED_PORT, LOW)

    print('done.')

if __name__ == '__main__':
    hostname = 'localhost'
    if len(sys.argv) > 1:
        hostname = sys.argv[1]

    main(hostname)
