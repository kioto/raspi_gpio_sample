#
# 02_led_wiringpi_software_pwm_test.py
#

import sys
import wiringpi

LED_PORT = 18
PWM_RANGE = 100

def main(duty):
    # Software PWM
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(LED_PORT, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.softPwmCreate(LED_PORT, 0, PWM_RANGE)
    wiringpi.softPwmWrite(LED_PORT, duty)
    # LEDを30秒間点灯する
    wiringpi.delay(30000)

    wiringpi.softPwmStop(LED_PORT)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python %s <duty_cycle>' % sys.argv[0])
        exit()

    main(int(sys.argv[1]))
