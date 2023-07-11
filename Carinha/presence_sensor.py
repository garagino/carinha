from datetime import datetime
from threading import Thread
from gpiozero import MotionSensor

class PresenceSensor(Thread):
    def __init__(self, pir_sensor):
        Thread.__init__(self)

        self.pir_sensor = MotionSensor(pir_sensor)

    def sense(self):
        while True:
            self.pir_sensor.wait_for_motion()
            initial_time = datetime.now()
            #TODO: log initial interaction
            #TODO: activate presence

            self.pir_sensor.wait_for_no_motion()
            delta_time = datetime.now() - initial_time
            self.__log_time(initial_time, delta_time)

    def __log_time(self, initial_interaction, duration):
        #TODO: Save initial interacion time and duration in csv file
        pass

    def run(self):
        self.sense()
