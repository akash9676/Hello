From GPIO zero import LED
From GPIO zero import Button
From time import sleep
Import Adafruit_DHT
Led=LED(24)
Button=Button(25)
Sensor=Adafruit_DHT.DHT11
GPIO=4
Humidity,temperature=Adafruit_DHT.lead_retry(sensor,GPIO)
While True:
      If humidity is not none and temperature is not none:
Button.wait_for_press()
Led.on()
Button.wait_for_release()
Led.off()
      Print(“temp={0:0.1f}*c humidity={1:0:1f}%”.format(temperature,humidity))
else:
print(“Failed to get reading.Try again”)
sleep(15)
