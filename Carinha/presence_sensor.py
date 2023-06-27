from threading import Thread
from time import sleep
import RPi.GPIO as GPIO  

class PresenceSensor(Thread):
    def __init__(self, pir_sensor):
        Thread.__init__(self)
        self.pir_sensor = pir_sensor
        self.presence = 0

        GPIO.setup(self.pir_sensor, GPIO.IN)

    def sense(self):
        timer = 0
        while True:
            if GPIO.input(self.pir_sensor):
                timer += 1
                sleep(1)
            else:
                timer = 0
            
            if timer >= 3:
                self.presence += 1

    def run(self):
        self.sense()
