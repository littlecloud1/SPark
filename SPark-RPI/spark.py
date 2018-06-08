import time
import RPi.GPIO as gpio
from ajaxCall import *
import serial
from dis_sensor import *
from gpiozero import Buzzer
#from detect import *

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
GPIO.setwarnings(False)
gpio.setup(16, gpio.OUT) #Green LED
gpio.setup(21, gpio.OUT) #Red LED
buzzer = Buzzer(17) #buzzer

ser=serial.Serial("/dev/ttyUSB0", 9600)
ser.baudrate = 9600
store = []
available = 1
    
while (1):  
    gpio.output(16, gpio.HIGH)
    gpio.output(21, gpio.LOW)
    data = ser.readline()
    light = int(data)
    print('The light sensor value is: %d' % light)
    dis=distance()
    print('The distance sensor value is: %.1f cm' % dis)
    
    if light > 500 and int(dis)< 30: #use both sensor to detect car
        print("Car detected!")
        time.sleep(1)
        id = getCarPlate(1)  #get the plate number from server
        id = str(id, 'utf-8')
        plate=id.upper()
        print("Plate number from server is: %s" % (plate) )
        time.sleep(0.5)
        #execfile('detect.py') #get the actual plate number
        actualplate = 'TEST1'
        
        print("The actual plate number is: %s" % (actualplate))
        time.sleep(0.5)
        if plate == actualplate:
            print("Matched!!")
            updateSensorStats(1,0,plate) #Update the availability of the spot to server
            gpio.output(16, gpio.LOW)
            gpio.output(21, gpio.HIGH)
            time.sleep(1)
        else:
            buzzer.on()
            print("not Matched!!")
            print("Remove the car or get a ticket")
            gpio.output(16, gpio.LOW)
            gpio.output(21, gpio.HIGH)
            time.sleep(4.5)
            gpio.output(16, gpio.HIGH)
            gpio.output(21, gpio.LOW)
            updateSensorStats(1,1,plate)
           
    else:
        print("no car")




