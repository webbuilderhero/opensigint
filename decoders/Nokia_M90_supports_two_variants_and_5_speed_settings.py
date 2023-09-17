"""Decoder for Nokia M/90"""

import numpy as np 

#TODO: Plug into SIGINT framework

#Variables to store speed settings
speed_one = 0
speed_two = 0 
speed_three = 0
speed_four = 0 
speed_five = 0 

#Variables to store variants
variant_one = [] 
variant_two = []


def decode_nokia_m90(input_signal):
    """Decode Nokia M/90 RF signal"""
    
    #Initialize output array to store decoded signals
    output_signal = np.array([])
    
    #Determine wave length of signal
    wl = len(input_signal)

    #Separate variants
    variant_one = input_signal[0:int(wl/2)]
    variant_two = input_signal[int(wl/2):wl]

    #Determine speed settings
    speed_one = len(variant_one)//5
    speed_two = len(variant_one)//4
    speed_three = len(variant_one)//3
    speed_four = len(variant_one)//2
    speed_five = len(variant_one)

    #Calculate the decoded signal from each variant
    for i in range(len(variant_one)):
        signal = variant_one[i] + variant_two[i]
        output_signal = np.append(output_signal, signal)
    
    return output_signal