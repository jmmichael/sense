#https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/2015/09/24/foginator-2000-003-raspberry-pi-sense-hat-integration-with-initial-state

from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

var = 30

while var > 0:
  temp = sense.get_temperature()
  temp = round(temp, 1)
  print("Temperature C",temp)
  humidity = sense.get_humidity()
  humidity = round(humidity, 1)
  print("Humidity :",humidity)
  pressure = sense.get_pressure()
  pressure = round(pressure, 1)
  print("Pressure:",pressure)
  time.sleep(1)
  var = var -1
  if var == 0:
    sys.exit()
