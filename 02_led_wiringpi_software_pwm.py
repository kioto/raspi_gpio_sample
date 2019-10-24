#
# 02_led_wiringpi_softpwm.py
#

import wiringpi

LED_PORT = 18
PWM_RANGE = 100

# Software PWM
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(LED_PORT, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.softPwmCreate(LED_PORT, 0, PWM_RANGE)

# LEDを2秒間点灯する
for duty in (5, 20, 50, 80, 100):
    print(duty)
    wiringpi.softPwmWrite(LED_PORT, duty)
    wiringpi.delay(2000)


wiringpi.softPwmStop(LED_PORT)

print('done')
