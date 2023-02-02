#from https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python#17657304
import time
import RPi.GPIO as GPIO
import pyaudio  
import wave

#Button pin definition
btn1_pin = 2
btn2_pin = 3

#Set up Pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn1_pin, GPIO.IN)
GPIO.setup(btn2_pin, GPIO.IN)

current_state1 = True
prev_state1 = True
playing_state1 = False
prev_playing_state1 = False

current_state2 = True
prev_state2 = True
playing_state2 = False
prev_playing_state2 = False

playSound = False
stopSound = True

#define stream chunk   
chunk = 1024  

#open a defalt wav format music  
f = wave.open("dogyInWindow.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()), 
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
 
try:

    while True:
        current_state1 = GPIO.input(btn1_pin)
        current_state2 = GPIO.input(btn2_pin)
        
        # change play state for each reagion
        if (current_state1 == False) and (prev_state1 == True):
            playing_state1 = not playing_state1
            prev_state1 = current_state1
        if (current_state1 == True) and (prev_state1 == False): #acknowledge button release
            prev_state1 = current_state1
            
        if (current_state2 == False) and (prev_state2 == True):
            playing_state2 = not playing_state2
            prev_state2 = current_state2
        if (current_state2 == True) and (prev_state2 == False):
            prev_state2 = current_state2
        
        #set reachion playstate as system play
        if (playing_state1 == True) and (prev_playing_state1 == False):
            playSound = True
            stopSound = False
            f = wave.open("saintsMarchingIn.wav","rb")  
            #stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            #    channels = f.getnchannels(),  
            #    rate = f.getframerate(),  
            #    output = True)  
            #read data  
            data = f.readframes(chunk)  
            prev_playing_state1 = playing_state1
            
        if (playing_state1 == False) and (prev_playing_state1 == True):
            stopSound = True
            playSound = False
            prev_playing_state1 = playing_state1
            
            
        if (playing_state2 == True) and (prev_playing_state2 == False):
            playSound = True
            stopSound = False
            f = wave.open("dogyInWindow.wav","rb")  
            #stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
            #    channels = f.getnchannels(),  
            #    rate = f.getframerate(),  
            #    output = True)  
            #read data  
            data = f.readframes(chunk)  
            prev_playing_state2 = playing_state2
            
        if (playing_state2 == False) and (prev_playing_state2 == True):
            stopSound = True
            playSound = False
            prev_playing_state2 = playing_state2
               
            
        # enact system state    
        if(playSound == True):
            stream.start_stream()
            stream.write(data)  
            data = f.readframes(chunk) 
        if(stopSound == True):
            stream.stop_stream()
            #stream.close()


#when you press ctrl +c (curently not responsive)
finally:
    GPIO.cleanup()
    #close PyAudio
    p.terminate()  
