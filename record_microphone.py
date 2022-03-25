import sounddevice as sd
from scipy.io.wavfile import write
import os

i = 0
while os.path.exists("output%s.wav" % i):
    i+=1


fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output%s.wav' % i, fs, myrecording)  # Save as WAV file 