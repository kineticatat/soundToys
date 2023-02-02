import time
import RPi.GPIO as GPIO
from pygame import mixer


#Button pin definition
btn1_pin = 2
#led_pin = 3
btn2_pin = 3

#Set up Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1_pin, GPIO.IN)
GPIO.setup(btn2_pin, GPIO.IN)
#GPIO.setup(led_pin, GPIO.OUT)


mixer.init()

current_state1 = True
prev_state1 = True

current_state2 = True
prev_state2 = True

file = mixer.Sound('/home/pi/file1.wav')
file2 = mixer.Sound('/home/pi/DanceScore1.wav')

try:

    while True:
        current_state1 = GPIO.input(btn1_pin)
        if (current_state1 == False) and (prev_state1 == True):
            file.play()
            #GPIO.output(led_pin, True)
            prev_state1 = current_state1
            
        if (current_state1 == True) and (prev_state1 == False):
            file.stop()
            #GPIO.output(led_pin, False)
            prev_state1 = current_state1
        
        current_state2 = GPIO.input(btn2_pin)
        if (current_state2 == False) and (prev_state2 == True):
            file2.play()
            #GPIO.output(led_pin, True)
            prev_state2 = current_state2
            
        if (current_state2 == True) and (prev_state2 == False):
            file2.stop()
            #GPIO.output(led_pin, False)
            prev_state2 = current_state2
#when you press ctrl +c
finally:
    GPIO.cleanup()

