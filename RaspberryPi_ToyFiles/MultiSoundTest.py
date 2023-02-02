import pygame
import time
import random
#note that there is a pygame music function
# but this only allows single channel (because it is streamed)
# it is possible to play music files over sound files
#this implyes that sound is played from ram so needs to
#consider file size of all file to be played
# files can be replayed

#pygame.init()
pygame.mixer.init()
#######################################
count = pygame.mixer.Sound("file1.wav")
music = pygame.mixer.Sound("dogyInWindow.wav")

#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

#plays multiple files when read, simultaneously
##can use count as delay, or delay, or if last !< current, etc
while True:
        id, text = reader.read()
        
        if id == (576445216648):
            print ('Tag 1 Found')
            pygame.mixer.Sound.play(count)
            time.sleep(2)
            continue
        
        elif id == (561186360885):
            print ('Tag 2 Found')
            pygame.mixer.Sound.play(music)
            time.sleep(2)
            continue
        
        elif id == (427164244981):
            print ('Tag 3 Found')
            time.sleep(2)
            pygame.mixerfadeout
            
              
##        elif id == ():
#            print ('Tag 4 Stick Found')
#            pygame.mixer.Sound.play(music)
 #           time.sleep(2)
 #           continue
        
####################################
#pygame.mixer.music.load("dogyInWindow.wav")
#pygame.mixer.music.play(2)
#pygame.mixer.music.load("file1.wav")
#pygame.mixer.music.play(2)


GPIO.cleanup()
