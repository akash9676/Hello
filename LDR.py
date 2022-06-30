import RPI.GPIO as GPIO
GPIO. Setmode(GPIO.BCM)
GPIO. Setwarnings(False)
GPIO. Setup(3, GPIO.OUT)
GPIO. Setup(2, GPIO.IN)
while True:
    Val = GPIO.input(2)
    if Val == 1:
        GPIO. output(3, True)
    else:
        GPIO. output(3, False)
