#
# 02_led_pwm.py
#

import RPi.GPIO as GPIO
import time

LED_PORT = 18
PWM_FREQUENCY = 500             # Hz

GPIO.setmode(GPIO.BCM)          # GPIO番号で指定
GPIO.setup(LED_PORT, GPIO.OUT)

# PWM
pwm = GPIO.PWM(LED_PORT, PWM_FREQUENCY)
pwm.start(0)

# LEDを2秒間点灯する
for duty in (5, 20, 50, 80, 100):
    print(duty)
    pwm.ChangeDutyCycle(float(duty))
    time.sleep(2)


GPIO.cleanup()

print('done')
