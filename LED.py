#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

a = str(raw_input())

LedPin = [11,13,15,16,18,29,31,33] # assign GPIO Pin numbers

GPIO.setmode(GPIO.BOARD) # Numbers pins by physical location

for i in xrange(8):
        GPIO.setup(LedPin[i], GPIO.OUT) # Set pin mode as output
        GPIO.output(LedPin[i], GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off

try:
        
        print "Binary: " + a

        for i in xrange(8):
                if a[7-i] == '1':
                        GPIO.output(LedPin[i], GPIO.LOW) # LED on
                else:
                        GPIO.output(LedPin[i], GPIO.HIGH)# LED off
                
        time.sleep(3) # Keep LED on for 3 seconds

        for i in xrange(8):
                GPIO.output(LedPin[i], GPIO.HIGH)

        GPIO.cleanup() #Release Resource

except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.

        for i in xrange(8):
                GPIO.output(LedPin[i], GPIO.HIGH) #LED off
        
	GPIO.cleanup()                     # Release resource

