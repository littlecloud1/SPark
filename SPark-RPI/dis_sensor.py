import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger 
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    beginTime = time.time()
    returnTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        beginTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        returnTime = time.time()

    timeTraveld = returnTime - beginTime
    #compute actual distance
    dis = (timeTraveld * 34300) / 2
 
    return dis
         
'''while (1):            
    dist = distance()
    #print ("The Distance is %.1f cm" % dist) 
    time.sleep(0.5)'''