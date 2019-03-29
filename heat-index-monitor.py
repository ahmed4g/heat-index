import time
import smbus2
import bme280
import RPi.GPIO as GPIO
from heat_index import heat_index
port = 1
address = 0x76
bus = smbus2.SMBus(port)
GPIO.setmode(GPIO.BCM)
green=26
yellow=19
orange=13
red=6
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(orange, GPIO.OUT)
calibration_params = bme280.load_calibration_params(bus, address)
# the sample method will take a single reading and return a
# compensated_reading object
while True:
   data = bme280.sample(bus, address, calibration_params)
   # calculate Heat Index
   hi = heat_index(temperature=data.temperature, humidity=data.humidity)
   if hi < 27:
       print ("safe")
       print ('Heat Index :', hi)
   elif hi>=27 and hi<32:
       print ("green")
       print ('Heat Index :', hi)
       GPIO.output(green, GPIO.HIGH)
       GPIO.output(yellow, GPIO.LOW)
       GPIO.output(orange, GPIO.LOW)
       GPIO.output(red, GPIO.LOW)
   elif hi>=32 and hi<39:
       print ("yellow")
       print ('Heat Index :', hi)
       GPIO.output(green, GGPIO.LOW)
       GPIO.output(yellow, GPIO.HIGH)
       GPIO.output(orange, GPIO.LOW)
       GPIO.output(red, GPIO.LOW) 
   elif hi>=39 and hi<50:
       print ("orange")
       print ('Heat Index :', hi)
       GPIO.output(green, GPIO.LOW)
       GPIO.output(yellow, GPIO.LOW)
       GPIO.output(orange, GPIO.HIGH)
       GPIO.output(red, GPIO.LOW)
   elif hi>=50 and hi<=53:
       print ("orange danger")
       print ('Heat Index :', hi)
       GPIO.output(green, GPIO.LOW)
       GPIO.output(yellow, GPIO.LOW)
       GPIO.output(orange, GPIO.HIGH)
       GPIO.output(red, GPIO.LOW)
   else:
       print ("red exteme")
       print ('Heat Index :', hi)
       GPIO.output(green, GPIO.LOW)
       GPIO.output(yellow, GPIO.LOW)
       GPIO.output(orange, GPIO.LOW)
       GPIO.output(red, GPIO.HIGH)
   time.sleep(10)
