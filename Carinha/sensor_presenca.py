#import RPi.GPIO as gpio # Comentado para não ficar acusando erro, só funciona na rasp
import time

pirSensor = 11
led = 7

gpio.setmode(gpio.BOARD) # Setamos o modo da rasp para usarmos a numeração fisica

gpio.setup(led, gpio.OUT) # Seta a variavel led para o modo de "saída"
gpio.setup(pirSensor, gpio.IN) # Seta a variavel pirSensor para o modo de "entrada"

presence = 0 # Inicializa a variavel de presença. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento 

# Um ciclo para verificar se houve movimento
try:
    while True: # Inicia um loop infinito 
        time.sleep(0.1) 
        presence = gpio.input(pirSensor) # atribui o valor do sensor pir à variavel presence. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento
        
        if presence: # Se houve movimento...
            print(f'Sensor PIR = {presence}')
            gpio.output(led, True) # Acende o led...
            time.sleep(1) # Aguardo um segundo...
            gpio.output(led, False) # E apaga
            time.sleep(3) # Após 3 segundos o processo se reinicia

except KeyboardInterrupt: # Caso seja pressionado Ctrl + C para interromper o programa vai sair do loop infinito
    pass
finally: 
    gpio.cleanup() # E vai executar o cleanup para limpar os pinos GPIO


