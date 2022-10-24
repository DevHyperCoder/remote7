import time

import RPi.GPIO as GPIO

from remote7.constants import chars
from remote7.utils import *

class SevenSegmentDriver:
    def __init__(self,pins,ca = True):
        self.ca = ca
        self.pins = pins

        GPIO.setmode(GPIO.BOARD)

        # Set GPIO pins to output mode and turn all leds 
        for l in self.pins.values():
            GPIO.setup(l, GPIO.OUT)
            self.off(l)

    def off(self,pin):
        GPIO.output(pin, self.ca)

    def on(self,pin):
        GPIO.output(pin, not self.ca)

    def set(self,pin,val):
        if val:
            self.on(pin)
        else:
            self.off(pin)

    def set_all_pins(self,val):
        for p in self.pins.values():
            self.set(p,val)

    def turn_off(self):
        self.set_all_pins(False)

    def display(self,msg, delay=0.5):
        if len(msg) > 1:
            for i in msg:
                if i not in chars:
                    raise_exception()
        elif msg not in chars:
            raise_exception()

        for ch in msg:
            for idx, i in enumerate("abcdefg"):
                v = chars[ch]
                op = int(format(v, "07b")[idx])
                self.set(self.pins[i], not not op)
            time.sleep(delay)

    def blink_all(self,delay):
        self.set_all_pins(True)
        time.sleep(delay)
        self.set_all_pins(False)

    def show_pattern(self,delay):
        pstr = "fabcdeg"

        for i in pstr:
            self.set(self.pins[i], True)
            time.sleep(delay)

        time.sleep(delay * 2)

        for i in pstr[::-1]:
            self.set(self.pins[i], False)
            time.sleep(delay)


