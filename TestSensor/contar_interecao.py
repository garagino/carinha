import RPi.GPIO as gpio # Comentado para não ficar acusando erro, só funciona na rasp

def millis():
    import time
    """Returns the current time in milliseconds"""

    return int(time() * 1000)

pirSensor = 40
led = 10

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

        if presence:  # Se houve movimento...
            if medir == 0: #pegar o tempo apenas uma vez
                tempo_inicio = millis();
                medir = 1
            else:  
                gpio.output(led, True)  # Acende o led...
                print('Ligado')
        else:
            tempo_fim = millis();
            medir = 0;
            gpio.output(led, False)  # E apaga
            print('Desligado')
            tempo_total = tempo_fim - tempo_inicio
            if tempo_total >= 5000: #Se o tempo da interação for maior que 10 segundos, adiciona +1 em uma interação
                interacoes+=1
            
except:  # Caso seja pressionado Ctrl + C para interromper o programa vai sair do loop infinito
    gpio.cleaup()
    print('Finalizando o C.A.R.I.N.H.A.\n')
    print(f'Interacoes: {interacoes}\n')
    

