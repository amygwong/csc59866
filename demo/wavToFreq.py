from scipy.io import wavfile
import numpy as np
from scipy import stats
from scipy.fftpack import fft
import wave

filename = "microphone-results.wav"

sample_rate, data = wavfile.read(filename)


fs, data = wavfile.read(filename) # load the data
a = data # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = fft(b) # calculate fourier transform (complex numbers list)
d = int(len(c)/2)

freqs = abs(c[:(d-1)])
freqs = [i/1000 for i in freqs if i < 280]

meanfreq = np.mean(freqs)
sd = np.std(freqs)
median = np.median(freqs)
q75, q25 = np.percentile(freqs, [75 ,25])

print(meanfreq,sd,median,q25,q75)


