import pyaudio
import wave
import array #array is faster then the original frames = [] call

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file1.wav"

audio = pyaudio.PyAudio()

print(audio.get_device_info_by_index(0)['defaultSampleRate'])

#start Recording
stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer=CHUNK)
print ("recording....")

try:
    data = array.array('h')

    for i in range(0, int((RATE / CHUNK) * RECORD_SECONDS)):
        data.fromstring(stream.read(CHUNK))
        
finally:
    #stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

print ("finished recording")

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
#waveFile.writeframes(b''.join(frames))
waveFile.writeframes(data)
waveFile.close()
