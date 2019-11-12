#
# 02_led_pigpio_software_pwm_test.py
#

import sys
import time
import pigpio

LED_PORT = 18
RANGE = 100

def main(freq, duty):
    # Software PWM
    pi = pigpio.pi()
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
    if len(sys.argv) != 3:
        print('Usage: python %s <frequency> <duty_cycle>' % sys.argv[0])
        exit()

    main(int(sys.argv[1]), float(sys.argv[2]))
