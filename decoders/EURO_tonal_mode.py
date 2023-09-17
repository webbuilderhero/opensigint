"""
Decoder for Euro Tonal Mode

Assumes input is a complex signal already in baseband

Initialize key parameters
"""
f_sample = 100.0  # Sampling frequency in Hz
f_deviation = 25.0  # Modulation deviation in Hz

"""
Define the functions needed
"""

# Calculate signal power
def power(signal):
    return math.sqrt(np.mean(np.abs(signal)**2))

# Find the peaks of the signal
def peakfinding_euro(signal):
    peakindexes = np.where( np.diff(signal) > 1e-7 )[0] # Find all rising causes
    peakindexes = np.append( peakindexes,
        np.where( np.diff(signal) < -1e-7 )[0] ) # Appending all falling edges
    peakindexes.sort()
    peakindexes = np.array(
        [ index for index in peakindexes if signal[index-1] <= signal[index] and signal[index] >= signal[index+1] ] ) # Remove all but peaks
 
    return peakindexes

# Calculate the baud rate
def baud_calc(signal):
    peak_indexes_res = peakfinding_euro(signal)
    # Calculate number of complete bauds
    n_bauds = (len(signal))/len(peak_indexes_res)
    # Calculate symbol rate from baud rate
    symbol_rate = n_bauds * f_sample
 
    return symbol_rate

# Decode the signal
def euro_decode(signal):
    # Calculate symbol rate
    symbol_rate = baud_calc(signal)
    # Calculate threshold value
    th = power(signal)/math.sqrt(2)
    data_level = np.where(signal > th, 1, 0)
 
    return (data_level, symbol_rate)

# Main function
def euro_mode_decode(signal):
    # Call decode 
    data, symbol