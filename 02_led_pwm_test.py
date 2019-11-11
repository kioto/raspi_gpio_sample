#
# 02_led_pwm_test.py
#

import sys
import RPi.GPIO as GPIO
import time

LED_PORT = 18

def main(freq, duty):
    GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
    GPIO.setup(LED_PORT, GPIO.OUT)

    # PWM
    pwm = GPIO.PWM(LED_PORT, freq)
    pwm.start(duty)

    # LEDを30秒間点灯する
    time.sleep(30)

    GPIO.cleanup()
    print('done')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python %s <frequency> <duty_cycle>' % sys.argv[0])
        exit()

    main(int(sys.argv[1]), float(sys.argv[2]))
