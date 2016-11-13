#!/usr/bin/env python

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

continue_reading = True

# start binary GPIO display    
LedPin = [11,13,15,16,18,29,31,33] # assign GPIO Pin numbers

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Ready to scan..."
print "Press Ctrl-C to stop.\n\n"

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])

        a = str(bin(uid[0]))[2:] #convert uid to binary

        GPIO.setmode(GPIO.BOARD) # Numbers pins by physical location

        for i in xrange(8):
            GPIO.setup(LedPin[i], GPIO.OUT) # Set pin mode as output
            GPIO.output(LedPin[i], GPIO.HIGH) # Set pin to high (+3.3V) to turn LED off

        #make sure a is of length 8
        for i in xrange(8-len(a)):
            a = '0' + a

        try:
            print "Binary: " + a

            for i in xrange(8):
                if a[7-i] == '1':
                    GPIO.output(LedPin[i], GPIO.LOW) # LED on
                else:
                    GPIO.output(LedPin[i], GPIO.HIGH)# LED off

            time.sleep(5) # Keep LED on for 5 seconds
            print "Lights off...\nReady to scan again...\n\n"

            for i in xrange(8):
                GPIO.output(LedPin[i], GPIO.HIGH)

            GPIO.cleanup() #Release Resource

        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.

            for i in xrange(8):
                GPIO.output(LedPin[i], GPIO.HIGH) #LED off
            GPIO.cleanup()                     # Release resource 
                                                                                                
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"

