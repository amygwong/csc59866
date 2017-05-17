from scipy.io import wavfile
import numpy as np
from scipy import stats
from scipy.fftpack import fft
import wave
import matplotlib.pyplot as plt
import math
filename = "microphone-results.wav"

sample_rate, data = wavfile.read(filename)


fs, data = wavfile.read(filename) # load the data
a = data # this is a two channel soundtrack, I get the first track
b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
c = np.fft.fft(b) # calculate fourier transform (complex numbers list)
d = int(len(c)/2)
c = abs(c[:(d-1)])

freqs = np.fft.fftfreq(len(c),1/fs)
vals = []
newfreqs = []
amps = []
for a,b in zip(freqs,c):
    if a<280 and a>0:
        vals.append(a*b/1000)
        newfreqs.append(a/1000)
        amps.append(b)
#vals = [a*b/1000 if a <280  for a,b in zip(freqs,c)]
#freqs = [i*fs/(len(data)*1000) for i in freqs if i*fs/len(data) < 280]

#calculate the mean
n = sum(amps)
meanfreq = sum(vals)/n

#calculate the standard deviation
sd = 0
for ind,i in enumerate(vals):
    sd = sd + (amps[ind]*newfreqs[ind]*newfreqs[ind])
sd = math.sqrt((sd-n*(meanfreq**2))/n)

#calculate the median
sum = 0
mid = n/2
currInd = 0
#sort the frequencies
newfreqs, amps = zip(*sorted(zip(newfreqs, amps)))
for ind, i in enumerate(amps):
    sum = i + sum
    if sum > mid:
        currInd = ind
        break
median = newfreqs[currInd]

#calculate the q25 <----------------
qnewfreqs = newfreqs[0:currInd]
qamps = amps[0:currInd]
qmid = np.sum(qamps)/2
qInd = 0
sum = 0
for ind, i in enumerate(qamps):
    sum = i + sum
    if sum > qmid:
        qInd = ind
        break
q25 = newfreqs[qInd]


q75 = 0 #<-------
print(meanfreq,',',sd,',',median,',',q25,',',q75)


