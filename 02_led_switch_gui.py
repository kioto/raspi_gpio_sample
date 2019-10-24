#
# 02_led_switch_gui.py
#

import tkinter
import RPi.GPIO as GPIO
import time

DEFAULT_SWITCH_PORT = 23
DEFAULT_LED_PORT = 18

class LedSwitchGUI(object):
    
    def __init__(self,
                 switch_port=DEFAULT_SWITCH_PORT, led_port=DEFAULT_LED_PORT):
        # GPIO
        self._switch_port = switch_port
        self._led_port = led_port
        GPIO.setmode(GPIO.BCM)  # GPIO番号で指定
        GPIO.setup(self._switch_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self._led_port, GPIO.OUT)
        GPIO.add_event_detect(self._switch_port, GPIO.BOTH,
                              callback=self.cb_switch)

    def run(self):
        # GUI
        self._root = tkinter.Tk()
        self._root.wm_title('Switch Monitor')
        self._root.geometry('200x100')
        # Frame
        frame = tkinter.Frame(self._root)
        frame.pack()
        # Message
        self._message = tkinter.StringVar()
        self._message.set('Ready')
        label = tkinter.Label(frame,
                              textvariable=self._message, font=('', 30))
        label.pack()
        # Quit button
        button = tkinter.Button(frame, text='Quit', command=self.quit_gui)
        button.pack()
        
        self._root.mainloop()

    def cb_switch(self, ch):
        self._state = GPIO.input(ch)
        if self._state:
            self._message.set('OFF')
            GPIO.output(self._led_port, False)
        else:
            self._message.set('Pushed')
            GPIO.output(self._led_port, True)

    def quit_gui(self):
        GPIO.cleanup()
        exit()

    
if __name__ == '__main__':
    app = LedSwitchGUI()
    app.run()
