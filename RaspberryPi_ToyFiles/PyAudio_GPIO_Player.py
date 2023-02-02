
#from https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python#17657304
import time
import RPi.GPIO as GPIO
import pyaudio  
import wave

#Button pin definition
btn1_pin = 2
#led_pin = 3
btn2_pin = 3

#Set up Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1_pin, GPIO.IN)
GPIO.setup(btn2_pin, GPIO.IN)
#GPIO.setup(led_pin, GPIO.OUT)

current_state1 = True
prev_state1 = True

current_state2 = True
prev_state2 = True

playSound = False
stopSound = True

#define stream chunk   
chunk = 1024  

#open a defalt wav format music  
f = wave.open("test.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()), 
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
#_data = f.readframes(chunk)  

#play stream  
#_while data:  
    #_stream.write(data)  
    #_data = f.readframes(chunk)

#stop stream  
#_stream.stop_stream()  
#_stream.close()

try:

    while True:
        current_state1 = GPIO.input(btn1_pin)
        current_state2 = GPIO.input(btn2_pin)
        if (current_state1 == False) and (prev_state1 == True):
            playSound = True
            stopSound = False
            f = wave.open("file1.wav","rb")  
            #stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            #    channels = f.getnchannels(),  
            #    rate = f.getframerate(),  
            #    output = True)  
            #read data  
            data = f.readframes(chunk)  
            #GPIO.output(led_pin, True)
            prev_state1 = current_state1
            
        if (current_state1 == True) and (prev_state1 == False):
            stopSound = True
            playSound = False
            #GPIO.output(led_pin, False)
            prev_state1 = current_state1
            
            
        if (current_state2 == False) and (prev_state2 == True):
            playSound = True
            stopSound = False
            f = wave.open("test.wav","rb")  
            #stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            #    channels = f.getnchannels(),  
            #    rate = f.getframerate(),  
            #    output = True)  
            #read data  
            data = f.readframes(chunk)  
            #GPIO.output(led_pin, True)
            prev_state2 = current_state2
            
        if (current_state2 == True) and (prev_state2 == False):
            stopSound = True
            playSound = False
            #GPIO.output(led_pin, False)
            prev_state2 = current_state2
               
            
            
        if(playSound == True):
            #stuff here
            stream.start_stream()
            stream.write(data)  
            data = f.readframes(chunk) 
        if(stopSound == True):
            #stuff here
            stream.stop_stream()
            #stream.close()


#when you press ctrl +c (curently not responsive)
finally:
    GPIO.cleanup()
    #close PyAudio
    p.terminate()  
