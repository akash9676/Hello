import RPI.GPIO as GPIO 
from time import sleep
GPIO. Setmode(GPIO.BCM)
GPIO. Setwarnings(False)
GPIO. Setup(3, GPIO.OUT)
GPIO. Setup(2, GPIO.OUT)
GPIO. Setup(4, GPIO.OUT)
while True:
    Val= GPIO. input(3, True)
    sleep(5)
    GPIO. output(3, False)
    GPIO. output(2, True)
    sleep(2)
    GPIO. output(2,False)
    GPIO. output(4, True)
    sleep(10)
    GPIO. output(4, False)
