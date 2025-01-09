import time

import RPi.GPIO as GPIO

#Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Set desired GPIO pins as outputs
crawlersForward = 11
crawlersBackward = 13
tilterLeft = 15
tilterRight = 16
GPIO.setup(crawlersForward, GPIO.OUT)
GPIO.setup(crawlersBackward, GPIO.OUT)
GPIO.setup(tilterLeft, GPIO.OUT)
GPIO.setup(tilterRight, GPIO.OUT)

#Turn off all motors
def allOff():
    GPIO.output(crawlersForward, GPIO.LOW) 
    GPIO.output(crawlersBackward, GPIO.LOW)
    GPIO.output(tilterLeft, GPIO.LOW)
    GPIO.output(tilterRight, GPIO.LOW)

#Begin with everything off
allOff()

try:
    while True:
        key = input("Enter W/A/S/D (or L to leave): ").lower()

        if key == 'w':
            print("Forward")
            GPIO.output(crawlersBackward, GPIO.LOW) #Prevent forward/backward being on at the same time
            GPIO.output(crawlersForward, GPIO.HIGH)

        elif key == 's':
            print("Backward")
            GPIO.output(crawlersForward, GPIO.LOW) #Prevent forward/backward being on at the same time
            GPIO.output(crawlersBackward, GPIO.HIGH)
                
        elif key == 'a':
            print("Left")
            GPIO.output(tilterRight, GPIO.LOW) #Prevent left/right being on at the same time
            GPIO.output(tilterLeft, GPIO.HIGH)

        elif key == 'd':
            print("Right")
            GPIO.output(tilterLeft, GPIO.LOW) #Prevent left/right being on at the same time
            GPIO.output(tilterRight, GPIO.HIGH)

        elif key == 'l':
            allOff()
            break

        else:
            allOff()
            print("Stopping")

finally:
    print("Program ended, cleaning up GPIO")
    GPIO.cleanup() #Reset GPIO settings        