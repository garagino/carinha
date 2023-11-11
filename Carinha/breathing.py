"""
    Breathing effect by lighting

    The lighting breathing effect aims to bring life and dynamism to the device,
    even when there is no one nearby interacting with it.
"""

from threading import Thread
from gpiozero import PWMLED
from time import sleep


class Breathing(Thread):
    """Thread that controls breathing"""
    def __init__(self, led_pin, frequency):
        Thread.__init__(self)

        self.frenquency = frequency
        self.led_pin = PWMLED(led_pin)
        self.sequence = list(range(0, 100)) + list(range(100, 0, -1))

    def breathe(self):
        """Executes the pulsation"""
        for intensity in self.sequence:
            self.led_pin.value = intensity / 100
            sleep(self.frenquency)

    def run(self):
        while True:
            self.breathe()

