import RPi.GPIO as gpio # Comentado para não ficar acusando erro, só funciona na rasp
import time
import os

def millis():
    
    """Returns the current time in milliseconds"""

    return int(time.time() * 1000)

pirSensor = 8
led = 12

# Setamos o modo da rasp para usarmos a numeração fisica
gpio.setmode(gpio.BOARD)

# Seta a variavel led para o modo de "saída"
gpio.setup(led, gpio.OUT)

# Seta a variavel pirSensor para o modo de "entrada"
gpio.setup(pirSensor, gpio.IN)

presence = 0  # Inicializa a variavel de presença. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento

# Um ciclo para verificar se houve movimento
try:
    medir = 0
    interacoes = 0
    
    while True:  # Inicia um loop infinito
        # atribui o valor do sensor pir à variavel presence. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento
        presence = gpio.input(pirSensor)

        if presence == 1:  # Se houve movimento...
            if medir == 0: #pegar o tempo apenas uma vez
                tempo_inicio = millis();
                medir = 1;
                print('Ligado')
            else:  
                gpio.output(led, True)  # Acende o led...
        else:
            gpio.output(led, False) # E apaga
            tempo_fim = millis();  
            
            if medir == 1: # Presença foi detectada previamente
                medir = 0  # Volta a situação original
                print('Desligado')
                tempo_total = tempo_fim - tempo_inicio
                if tempo_total >= 5000: #Se o tempo da interação for maior que 5 segundos, adiciona +1 em uma interação
                    interacoes+=1
            
except:  # Caso seja pressionado Ctrl + C para interromper o programa vai sair do loop infinito
    gpio.cleanup()
    print('\nFinalizando o C.A.R.I.N.H.A.\n')
    print(f'Interações: {interacoes}\n')
    


