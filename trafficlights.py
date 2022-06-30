Import RPI.GPIO as GPIO 
From time import sleep
GPIO. Set mode (GPIO.BCM)
GPIO. Set warnings (False)
GPIO. Set up (3, GPIO.OUT)
GPIO. Set up (2, GPIO.OUT)
GPIO. Set up (4, GPIO.OUT)
While True:
          Val= GPIO. input(3, True)
Sleep(5)
GPIO. output(3, False)
            GPIO. output(2, True)
Sleep(2)
            GPIO. output(2,False)
GPIO. output(4, True)
Sleep(10)
GPIO. output(4, False)
