#!/usr/bin/python3
import cv2 # Biblioteca OpenCV
import os # Biblioteca para operações do sistema
import time # Biblioteca de tempo
from picamera2 import Picamera2 # Biblioteca da câmera da Raspberry Pi

import RPi.GPIO as rpio
import time

led_pin = 27

#Configuração dos pinos no pacote RPi.GPIO
rpio.setmode(rpio.BCM)
rpio.setwarnings(False)
rpio.setup(led_pin, rpio.OUT)	#LED como saída
rpio.output(led_pin, False)	

# Carrega o classificador para detecção facial (informar o caminho do arquivo)
face_detector = cv2.CascadeClassifier( "/home/sel/8180/haarcascade_frontalface_default.xml" )

# Inicia uma thread para gerenciar janelas de visualização
cv2.startWindowThread()

# Inicializa a câmera da Raspberry Pi
picam2 = Picamera2()

picam2.configure(picam2.create_preview_configuration(main={ "format" :'XRGB8888' , "size" : ( 640 , 480 )}))

picam2.start()

output_directory = "detected_faces"

os.makedirs(output_directory, exist_ok=True)

while True:
	im = picam2.capture_array()
	grey = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(grey, 1.1 , 5 )

	#Se detectar um ou mais faces, então acende o LED, caso contrário, apaga
	print(len(faces))
	if(len(faces) > 0):
			
		rpio.output(led_pin, True)
	else:
		rpio.output(led_pin, False)

		
	cv2.imshow("Camera", im)
	
	cv2.waitKey(1)
