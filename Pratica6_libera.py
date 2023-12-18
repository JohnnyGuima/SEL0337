from mfrc522 import SimpleMFRC522
from time import sleep 
import RPi.GPIO as rpio



led1_pin = 27			
led2_pin = 22	

#Configuração dos pinos no pacote RPi.GPIO
rpio.setmode(rpio.BCM)
rpio.setwarnings(False)
rpio.setup(led1_pin, rpio.OUT)	#LED 1 como saída
rpio.setup(led2_pin, rpio.OUT)	#LED 2 como saída

#Inicializa os LEDs 1 e 2 apagados
rpio.output(led1_pin, False)	
rpio.output(led2_pin, False)

leitor = SimpleMFRC522()
ID_tag="631360431670"

print("Aproxime a tag do leitor para leitura:")
while True:
	
	leitura = leitor.read()
	print("ID:{}\nTexto: {}".format(leitura[0],leitura[1]))
	sleep(1) 
	
	if str(leitura[0])==ID_tag:
		rpio.output(led1_pin, True)
		rpio.output(led2_pin, False)
		print("Acesso LIberado")
	else:
		rpio.output(led2_pin, True)
		rpio.output(led1_pin, False)
		print("Acesso Negado")
