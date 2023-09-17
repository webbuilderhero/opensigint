"""
#TODO: Figure out signal hopping algorithm

import math

#Decoder for R&S ALIS v50 Hopping

# This function returns the next frequency to be used while hopping
def rsand_next_frequency(fc, channels, interval):
    
    #calculate step = (channels-1) * interval
    step = (channels-1) * interval

    # calculate upper and lower frequency in range
    f_upper = fc + (step/2)
    f_lower = fc - (step/2)

    # determine the next frequency to be used (using round off)
    # this is done by calculating the ceil and floor of f_upper and f_lower
    ceil_f_upper = math.ceil(f_upper)
    floor_f_lower = math.floor(f_lower)

    #returns the next frequency in the hopping sequence
    next_freq = (ceil_f_upper + floor_f_lower)/2

    return next_freq

#This function helps in getting cumulative frequency of a signal
def rsand_cumulative_frequency(fc, channels, interval):
    #initialise cumulative_freq
    cumulative_freq = fc
    #initialise step
    step = (channels-1) * interval

    #calculate upper limit for range and assign to upper_limit
    upper_limit = fc + (step/2)

    #Iterate over frequencies within the range
    while(cumulative_freq < upper_limit):
        cumulative_freq = cumulative_freq + interval
        yield cumulative_freq

# This function returns the next frequency to be used while hopping
# based on the cumulative frequency of the received signal
#fc: center frequency
#channels: number of channels
#interval: frequency hopping interval
def signal_hopping(fc, channels, interval):
    for cumulative_freq in rsand_cumulative_frequency(fc, channels, interval):
        next_freq = rsand_next_frequency(cumulative_freq, channels, interval)
        # Print Next Frequency
        print('Next Frequency: %