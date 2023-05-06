import RPi.GPIO as gpio  # Comentado para não ficar acusando erro, só funciona na rasp


pirSensor = 40
led = 10

# Setamos o modo da rasp para usarmos a numeração fisica
gpio.setmode(gpio.BOARD)

gpio.setup(led, gpio.OUT)  # Seta a variavel led para o modo de "saída"
# Seta a variavel pirSensor para o modo de "entrada"
gpio.setup(pirSensor, gpio.IN)

presence = 0  # Inicializa a variavel de presença. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento

# Um ciclo para verificar se houve movimento
try:
    while True:  # Inicia um loop infinito
        # atribui o valor do sensor pir à variavel presence. Quando for 0 -> nenhum movimento; Quando for 1 -> houve movimento
        presence = gpio.input(pirSensor)

        if presence:  # Se houve movimento...
            gpio.output(led, True)  # Acende o led...
            print('Ligado')
        else:
            gpio.output(led, False)  # E apaga
            print('Desligado')

except:  # Caso seja pressionado Ctrl + C para interromper o programa vai sair do loop infinito
    gpio.cleaup()
    print('Finalizando o C.A.R.I.N.H.A.')
