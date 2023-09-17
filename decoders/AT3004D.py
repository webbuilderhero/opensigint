# TODO: Look into exact specifications for this model

import sys

#Define global variables
FILTERED_FREQUENCY = 0
BIT_RATE = 0 

# Collecting data
def getData(data):
    '''
    Parameters:
        data (str) :RF signal in AT-3004D format
    Returns:
        signal_data (list): list of RF signal values 
    '''
    # Split data into values
    signal_data = data.split('-')
    
    return signal_data

# Analyzing data
def analyzeData(signal_data):
    '''
    Parameters:
        signal_data (list): list of RF signal values 
    Returns:
        None
    '''
    global FILTERED_FREQUENCY
    global BIT_RATE

    # TODO: Look into exact specifications for this model
    # Assuming frequencies and bitrates for AT-3004D
    FILTERED_FREQUENCY = 15.7
    BIT_RATE = 9.6 
    
    # Analyze frequency
    frequency_signal = signal_data[0]
    filtered_frequency = float(frequency_signal)
    # TODO: Validate filtered frequency against FILTERED_FREQUENCY

    # Analyze data rate
    bitrate_data = signal_data[1]

    # TODO: Validate bitrate_data against BIT_RATE
    
    # Collect any additional data needed
    # TODO: Add additional data parsing if required

# Decode data
def decodeData(signal_data):
    '''
    Parameters:
        signal_data (list): list of RF signal values passed from analyzeData func
    Returns:
        decoded_data (list): list of decoded RF signal values
    '''
    decoded_data = []

    # Decode data here 
    # TODO: Look into exact specifications for this model
    # Assuming data is in base 10 for AT-3004D
    for data in signal_data:
        decoded_data.append(int(data, 10))

    return decoded_