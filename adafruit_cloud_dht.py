import time
from Adafruit_IO import Client

import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
pin =24


ADAFRUIT_IO_USERNAME = 'put your username here'
ADAFRUIT_IO_KEY = 'put your key here'


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

tempx= aio.feeds('temperature')
humidity = aio.feeds('humidity')

while 1:
	hum, tem = Adafruit_DHT.read_retry(sensor, pin)
	print hum
	print tem
	print "---------------------"
	time.sleep(1)
	print "---------------------"
	aio.send(tempx.key, int(tem))
	aio.send(humidity.key, int(hum))
	time.sleep(3)



