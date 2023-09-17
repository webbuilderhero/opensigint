#TODO: Test if this script works and needs additional components 

'''
Decoder for R&S ALIS v10

This script decodes a R&S ALIS v10 signal and outputs the necessary information for signal intelligence. 
'''


#Import necessary packages 
import numpy as np 
import scipy.constants as const 
import scipy.signal as signal 
import math 

#Define necessary variables
fs=int(input("Please enter the value of sampling frequency of the input signal : "))

#Define the start and end frequencies
fstart=int(input("Please enter the start frequency of the signal (in Hz) : "))
fend=int(input("Please enter the end frequency of the signal (in Hz) : "))

#Define signal length
sig_len=int(input("Please enter the length of the signal : "))

#Create an empty array to store the signal data
data=np.zeros((sig_len,2))

#Read the signal data 
for i in range(sig_len):
	data[i,0]=(int(input("Please enter the real component of data point " + str(i+1) + " : ")))
	data[i,1]=(int(input("Please enter the imaginary component of data point " + str(i+1) + " : ")))

#Define the input signal parameters
f=np.linspace(fstart,fend,sig_len)

#Fourier transform the data for the input signal
fftData= np.fft.fft(data)

#Estimate and plot the variance in the signal
r=signal.periodogram(data, fs=fs)

#Calculate the noise power
noisePwr= 10* np.log10(const.k*fs* r[1].mean())

#Calculate the signal/noise ratio
signal_noise= 10*np.log10(np.sum(fftData**2)/r[1].mean())

#Print the signal/noise ratio
print("The S/