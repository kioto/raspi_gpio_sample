#
# 02_led_pigpio_hardware_pwm.py
#

import time
import pigpio

LED_PORT = 18
PWM_FREQUENCY = 500             # Hz

# Hardware PWM
pi = pigpio.pi()
pi.set_mode(LED_PORT, pigpio.OUTPUT)

# LEDを2秒間点灯する
for duty in (5, 20, 50, 80, 100):
    print(duty)
    pi.hardware_PWM(LED_PORT, PWM_FREQUENCY, duty * 10000)
    time.sleep(2)

# ピンをINPUTモードにしておかないと、LEDが点灯し続けてしまう
pi.set_mode(LED_PORT, pigpio.INPUT)
pi.stop()
