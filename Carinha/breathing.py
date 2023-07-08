"""Breathing effect by lighting

The lighting breathing effect aims to bring life and dynamism to the device,
even when there is no one nearby interacting with it.
"""

from threading import Thread
from time import sleep
import RPi.GPIO as GPIO


class Breathing(Thread):
    """Thread that controls breathing"""
    def __init__(self, led_pin, frequency):
        Thread.__init__(self)
        self.frenquency = frequency
        self.led_pin = led_pin
        self.sequence = list(range(0, 100)) + list(range(100, 0, -1))

        GPIO.setmode(GPIO.BOARD)
        GPIO.cleanup()
        GPIO.setup(self.led_pin, GPIO.OUT)

        self.pwm = GPIO.PWM(self.led_pin, 100)
        self.pwm.start(0)

    def breathe(self):
        """Executes the pulsation"""
        for intensity in self.sequence:
            self.pwm.ChangeDutyCycle(intensity)
            sleep(self.frenquency)

    def run(self):
        while True:
            self.breathe()


breathe = Breathing(8, 0.02)
