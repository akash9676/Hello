from GPIO zero import LED
from GPIO zero import Button
from time import sleep
import Adafruit_DHT
Led = LED(24)
Button = Button(25)
Sensor = Adafruit_DHT.DHT11
GPIO = 4
Humidity, temperature = Adafruit_DHT.lead_retry(Sensor, GPIO)
while True:
    if Humidity is not None and temperature is not None:
        Button.wait_for_press()
        Led.on()
        Button.wait_for_release()
        Led.off()
        print("temp={0:0.1f}*c humidity={1:0:1f}%" .format(temperature, Humidity))
    else:
        print("Failed to get reading.Try again")
        sleep(15)
