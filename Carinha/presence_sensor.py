from datetime import datetime
from threading import Thread
from os.path import exists
from csv import writer
from gpiozero import MotionSensor

from utils import LOG_TIME_FILE

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
        if not exists(LOG_TIME_FILE):
            with open(LOG_TIME_FILE, 'w', encoding='UTF-8') as file:
                log_file = writer(file)
                log_file.writerow(['initial_interaction', 'duration'])

        with open(LOG_TIME_FILE, 'a', encoding='UTF-8') as file:
            log_file = writer(file)
            log_file.writerow([initial_interaction, duration])

    def run(self):
        self.sense()
