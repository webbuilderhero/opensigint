#TODO: Research APD AI-010 Specifications 

#This is the framework for a RF Decoder script that reads in a stream of 1s and 0s from a frequency range pertinent to the APD AI-010 signal
import numpy as np 

#expect a bitstream of ones and zeroes
bitstream = []

#The bit rate for the APD AI-010 signal
bit_rate = 100 #bit/s

#initialize variables to track bits and flags 
code_bits = 0
code_flags = 0

#loop over the bitstream
for bit in bitstream:
	#determine if the bit is a 1 or a 0
	if bit == 1:
		code_flags += 1
	else:
		code_flags = 0
	#add the bit to the bit count
	code_bits += 1
	#if the bit count meets the bit rate, the code is complete
	if code_bits >= bit_rate:
		#check the flags to determine if it is a long or short APD AI-010 signal
		if code_flags == 1:
			print('Long APD AI-010 signal')
		else:
			print('Short APD AI-010 signal')
		#reset bit count and flags
		code_bits = 0
		code_flags = 0