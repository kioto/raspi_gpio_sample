#
# 02_led_wiringpi_hardware_pwm.py
#

import wiringpi

LED_PORT = 18                   # GPIO 18
PWM_RANGE = 100
# PWMコントローラの動作クロック周波数19.2MHz / PWM信号の周波数50Hz
CLOCK_BASE = int(19.2 * 1000 / 50.0)
print(CLOCK_BASE)

# Software PWM
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(LED_PORT, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetRange(PWM_RANGE)
wiringpi.pwmSetClock(CLOCK_BASE)

# LEDを2秒間点灯する
for duty in (5, 20, 50, 80, 100):
    print(duty)
    wiringpi.pwmWrite(LED_PORT, duty)
    wiringpi.delay(2000)


wiringpi.pwmWrite(LED_PORT, 0)

print('done')
