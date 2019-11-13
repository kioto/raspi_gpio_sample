#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import time
import pigpio

MOTOR_PORT = 19
WAIT_TIME = 1.0

# SG90
# 
# Position "0" (1.45 ms pulse) is middle,
# "90" (~2.4 ms pulse) is all the way to the right,
# "-90" (~ 0.5 ms pulse) is all the way left.

PWM_FREQUENCY = 50                     # Hz
PWM_CYCLE = 1/PWM_FREQUENCY * 1000     # ms
RANGE = 1000
DUTY_MIDDLE   = 1.45 / PWM_CYCLE * RANGE
DUTY_PLUS_90  = 2.4  / PWM_CYCLE * RANGE
DUTY_MINUS_90 = 0.5  / PWM_CYCLE * RANGE

def main(hostname):
    # Software PWM
    pi = pigpio.pi(hostname)
    pi.set_mode(MOTOR_PORT, pigpio.OUTPUT)
    pi.set_PWM_frequency(MOTOR_PORT, PWM_FREQUENCY)
    pi.set_PWM_range(MOTOR_PORT, RANGE)
    pi.set_PWM_dutycycle(MOTOR_PORT, DUTY_MIDDLE)
    time.sleep(WAIT_TIME)

    for i in range(2):
        for duty in [DUTY_MINUS_90,
                     DUTY_MIDDLE,
                     DUTY_PLUS_90,
                     DUTY_MIDDLE,]:
            print(duty)
            pi.set_PWM_dutycycle(MOTOR_PORT, duty)
            time.sleep(WAIT_TIME)

    pi.set_mode(MOTOR_PORT, pigpio.INPUT)
    pi.stop()

if __name__ == '__main__':
    hostname = 'localhost'
    if len(sys.argv) > 1:
        hostname = sys.argv[1]

    main(hostname)
