from scipy.io import wavfile
import numpy as np
from scipy import stats

filename = "microphone-results.wav"
sample_rate, data = wavfile.read(filename)

w = np.fft.fft(data)
freqs = np.fft.fftfreq(len(data))
for f in freqs:
    f = f / 1000
    print(f)

meanfreq = np.mean(freqs)
sd = np.std(freqs)
median = np.median(freqs)
q75, q25 = np.percentile(freqs, [75 ,25])
iqr = q75 - q25
skew = stats.skew(freqs)
kurt = stats.kurtosis(freqs)
