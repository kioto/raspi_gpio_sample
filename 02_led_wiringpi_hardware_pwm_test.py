#
# 03_led_wiringpi_hardware_pwm_test.py
#

import sys
import wiringpi

LED_PORT = 18                   # GPIO 18
PWM_RANGE = 1024
def main(freq, duty_cycle):
    # Hardware PWM
    clock_base = int(18750 / freq)
    wiringpi.wiringPiSetupGpio()
    wiringpi.pinMode(LED_PORT, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    wiringpi.pwmSetRange(PWM_RANGE)
    wiringpi.pwmSetClock(clock_base)
    wiringpi.pwmWrite(LED_PORT, int(PWM_RANGE * duty_cycle))

    # LEDを30秒間点灯する
    wiringpi.delay(30000)

    wiringpi.pwmWrite(LED_PORT, 0)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python %s <frequency> <duty_cycle>' % sys.argv[0])
        exit()

    main(int(sys.argv[1]), int(sys.argv[2])/100)
