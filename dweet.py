#https://www.youtube.com/watch?v=JwrC47kvc0Q Chris Vaden. Easy Sense Hat Dashboard
from sense_hat import SenseHat
import time
import requests

sense = SenseHat()

def readings():
    humidity = str(round(sense.get_humidity(),2))
    temp = str(round(sense.get_temperature(),2))
    pressure = str(round(sense.get_pressure(),2))
    url = 'https://dweet.io/dweet/for/sensehatjm?' + 'temp=' + temp + '&humidity=' + humidity + '&pressure=' + pressure
    r = requests.post(url)

while True:
    readings()
    time.sleep(3)
    print('readings')
