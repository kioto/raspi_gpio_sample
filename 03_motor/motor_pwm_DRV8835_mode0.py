#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import time
import RPi.GPIO as gpio

PIN_MODE = 2
PIN_AIN1 = 3
PIN_AIN2 = 4

FREQUENCY = 50

def normal_rotation(duty, rot_time):
    pwm = gpio.PWM(PIN_AIN1, duty)
    pwm.ChangeFrequency(FREQUENCY)
    gpio.output(PIN_AIN2, gpio.LOW)
    pwm.start(duty)
    time.sleep(rot_time)
    
def reverse_rotation(duty, rot_time):
    pwm = gpio.PWM(PIN_AIN2, duty)
    gpio.output(PIN_AIN2, gpio.LOW)
    gpio.output(PIN_AIN1, gpio.LOW)
    pwm.start(duty)
    time.sleep(rot_time)

def stop_rotation(rot_time):
    gpio.output(PIN_AIN1, gpio.LOW)
    gpio.output(PIN_AIN2, gpio.LOW)
    time.sleep(rot_time)
    
def motor(duty):
    gpio.setmode(gpio.BCM)
    gpio.setup(PIN_MODE, gpio.OUT)
    gpio.setup(PIN_AIN1, gpio.OUT)
    gpio.setup(PIN_AIN2, gpio.OUT)

    gpio.output(PIN_MODE, gpio.LOW)

    print('正転')
    normal_rotation(duty, 1)

    print('空転')
    stop_rotation(1)
    
    print('逆転')
    reverse_rotation(duty, 1)

    print('空転')
    stop_rotation(1)

    gpio.cleanup()
    

if __name__ == '__main__':
    duty = 8
    if(len(sys.argv) > 1):
        duty = int(sys.argv[1])

    motor(duty)
