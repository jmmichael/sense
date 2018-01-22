#https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/2015/09/24/foginator-2000-003-raspberry-pi-sense-hat-integration-with-initial-state

from sense_hat import SenseHat
import time
import sys
from ISStreamer.Streamer import Streamer


logger = Streamer(bucket_name="Sense Hat Environment Stream", access_key="Fdwur4IZ2OA2s1y5GL6dlXQmZOogsDC1")


sense = SenseHat()
sense.clear()
var = 30


while var > 0:
  temp = sense.get_temperature()
  temp = round(temp, 1)
  logger.log("Teperature C",temp)
  humidity = sense.get_humidity()
  humidity = round(humidity, 1)
  logger.log("Humidity :",humidity)
  pressure = sense.get_pressure()
  pressure = round(pressure, 1)
  logger.log("Pressure:",pressure)
  var = var -1
  time.sleep(30)
  if var == 0:
    sys.exit()
