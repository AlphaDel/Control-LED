#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib, urllib, requests
from time import sleep
import RPi.GPIO as GPIO
import time
import string
GPIO.setmode(GPIO.BOARD)

led1 = 11
led2 = 13
led3 = 15

checkled1 = False
checkled2 = False
checkled3 = False

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


def main():

    while True:

   	baseURL = 'https://api.thingspeak.com/channels/115690/fields/1/last' 
	
        try:
		f = requests.get(baseURL)
		print f.text
		
                if f.text == '10':
                        GPIO.output(11, GPIO.HIGH) # led 1 off
                        print("led 1 off!!!")
                        checkled1 = False
                elif f.text == '11':
                        GPIO.output(11, GPIO.LOW)  # led 1 on
                        print ("led 1 on!!!")
                        checkled1 = True
                elif f.text == '20':
                        GPIO.output(13, GPIO.HIGH) # led 2 off
                        print("led 2 off!!!")
                        checkled2 = False
                elif f.text == '21':
                        GPIO.output(13, GPIO.LOW) # led 2 on
                        print("led 2 on!!!")
                        checkled2 = True
                elif f.text == '30':
                        GPIO.output(15, GPIO.HIGH) # led 3 off
                        print("led 3 off!!!")
                        checkled3 = False
                elif f.text == '31':
                        GPIO.output(15, GPIO.LOW) # led 3 on
                        print("led 3 on!!!")
                        checkled3 = True
                elif f.text == '777':             # turn off all LED
                        GPIO.output(11, GPIO.HIGH)
                        GPIO.output(13, GPIO.HIGH)
                        GPIO.output(15, GPIO.HIGH)
                        print("LED off all !!!")
                elif f.text == '999':             # turn on all LED   
                        GPIO.output(11, GPIO.LOW)
                        GPIO.output(13, GPIO.LOW)
                        GPIO.output(15, GPIO.LOW)
                        print("LED on all !!!")
                else:
                        print ("not found command")
                 
                print '==========================================='  	
                f.close()
            	sleep(5)
        except:
               print 'exit.'
               break;
        

if __name__ == "__main__":
    main()

