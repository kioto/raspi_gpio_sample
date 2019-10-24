#
# 02_led_pwm_test.py
#

import sys
import RPi.GPIO as GPIO
import time

LED_PORT = 18
PWM_FREQUENCY = 500             # Hz

def main(duty):
    GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
    GPIO.setup(LED_PORT, GPIO.OUT)

    # PWM
    pwm = GPIO.PWM(LED_PORT, PWM_FREQUENCY)
    pwm.start(duty)

    # LEDを30秒間点灯する
    time.sleep(30)

    GPIO.cleanup()
    print('done')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python %s <duty_cycle>' % sys.argv[0])
        exit()

    main(float(sys.argv[1]))
