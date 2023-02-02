#new wave player
import pyaudio
import wave

#define stream chunk   
#chunk = 1024  

#open a wav format music  
#f = wave.open("test.wav")
pa = pyaudio.PyAudio()
pa.get_default_output_device_info()
##wav_file = wave.open("file1.wav")
##wav_file = wave.open("test.wav")
wav_file = wave.open("file1.wav")
##wav_file = wave.open("DanceScore1.wav")

#instantiate PyAudio  
#p = pyaudio.PyAudio()  
#open stream  
#stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                #channels = f.getnchannels(),  
                #rate = f.getframerate(),  
                #output = True)
stream = pa.open(
    rate= wav_file.getframerate(),
    channels = wav_file.getnchannels(),
    format = pa.get_format_from_width(wav_file.getsampwidth()),
    output = True,
    #output_device_index = 4,
    #frames_per_buffer = 1024,
    )
frames_per_buffer = 1024
#read data  
#data = wav_file.readframes(frames_per_buffer)  

#play stream  
#while data:  
 #   stream.write(data)  
  #  data = wav_file.readframes(frames_per_buffer)
output_audio = wav_file.readframes(10 * wav_file.getframerate())
stream.write(output_audio)
#stop stream  
stream.stop_stream()  
stream.close()  