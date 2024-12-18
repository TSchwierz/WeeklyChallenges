'''
Challenge 1: Signal Processing - Noise Reduction
Context: 
You are given a noisy sine wave signal that simulates data collected from a sensor. The goal is to clean the signal using a low-pass filter.

Tasks:
Generate a noisy sine wave using NumPy (sin function + random noise).
Use SciPy to apply a low-pass filter to the signal.
Visualize the original noisy signal and the filtered signal using Matplotlib.
'''
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt

#Signal fields
T_MAX = 10 # time of the signal in seconds
n = 100 # number of data points
alpha = 0.3  # noise to signal ratio

#Filter fields + construction
fs = n/T_MAX # sampling fequency 
cutoff = 1. # cutoff frequency of the filter
order = 4 # Filter order
nyq = fs/2 #Nyquest frequency
b, a = butter(order, cutoff/nyq, btype='lowpass') # creating filter variables

t = np.linspace(0, T_MAX, n) # creating a timeline as signal input
signal = np.sin(t) + alpha*np.random.uniform(0,1,n) # create a noisy signal. 
filtered_signal = filtfilt(b, a, signal) # apply digital filter

plt.plot(t, signal, label='signal')
plt.plot(t, filtered_signal, label='filtered')
plt.xlabel('t(s)')
plt.ylabel('Amplitude(No Unit)')
plt.legend()
plt.show()