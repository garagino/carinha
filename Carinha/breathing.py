from threading import Thread
import RPi.GPIO as GPIO
from time import sleep


class Breathing(Thread):
    def __init__(self, frequency):
        Thread.__init__(self)
        self.frenquency = frequency

        self.led_pin = 0 # Colocar o número da porta aqui

        GPIO.setup(self.led_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(led_pin, 100)
        self.pwm.start(0)


    def breathe(self):
        for intensity in range(0, 101):
            self.pwm.ChangeDutyCycle(intensity)
            sleep(self.frenquency)
        
        for intensity in range(100, -1, -1):
            self.pwm.ChangeDutyCycle(intensity)
            sleep(self.frenquency)
    
    def run(self):
        self.breathe()


breathe = Breathing(0.5)

while True:
    breathe.run()

# NÃO SEI SE FUNCIONA
