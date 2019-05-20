import RPi.GPIO as GPIO
import dht11
import time

# import libraries 
from Adafruit_IO import *

aio = Client('','') #username and key respectively 
# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        aio.send("#dashboard name", Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    time.sleep(1)
