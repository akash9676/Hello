Import RPI.GPIO as GPIO 
GPIO. Set mode (GPIO.BCM)
GPIO. Set warnings (False)
GPIO. Set up (3, GPIO.OUT)
GPIO. Set up (2, GPIO.IN)
While True:
          Val= GPIO. input(2)
     If val ==1:
            GPIO. output(3, True)
    Else:
            GPIO. output(3,False)
