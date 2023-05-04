from gpiozero import MotionSensor, LED
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

pir = MotionSensor(21)
led = LED(15)

try:
    while True:
        pir.wait_for_motion()
        led.on()
        pir.wair_for_no_motion()
        led.off()
except:
    gpio.cleanup()
    print('Finalizando o C.A.R.I.N.H.A.!')