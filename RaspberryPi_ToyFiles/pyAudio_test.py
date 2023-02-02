
#from https://stackoverflow.com/questions/17657103/how-to-play-wav-file-in-python#17657304
import pyaudio  
import wave  

#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open("test.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)

#stop stream  
stream.stop_stream()  
stream.close()  


#when you press ctrl +c
finally:
    GPIO.cleanup()
#close PyAudio  
p.terminate()  
