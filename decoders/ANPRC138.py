#TODO - Include explanations for what each statement is doing

# AN/PRC-138 Decoder

# A decoder for the AN/PRC-138 radio frequency signal intelligence (sigint)

import sys

# Create a dictionary of all the known parameters for the AN/PRC-138
parameters = {
"frequency_low" : 300, 
"frequency_high" : 470, 
"signal_bandwidth" : 12.5, 
"modulation" : ["AM", "USB", "LSB", "CW", "ISB", "IQ"],
"voice_channels" : 10,
"data_channels" : 12
}

# Iterate through a list of sigint information
for sigint in sys.argv[1:]:

    # Extract the frequency and modulation from the sigint
    frequency = int(sigint.split(':')[0]) 
    modulation = sigint.split(':')[1]

    # Check to ensure that the frequency is within the expected range
    if frequency < parameters['frequency_low'] or frequency > parameters['frequency_high']:
        print("ERROR: Frequency is outside of valid range!") 

    # Check to ensure the modulation is valid
    elif modulation not in parameters["modulation"]:
        print("ERROR: Modulation is not valid!")

    # If passed the validity check, extract other parameters
    else: 
        # Calculate channel bandwidth
        channel_bandwidth = parameters['signal_bandwidth'] / parameters['voice_channels']

        # Calculate center frequency of transmitted signal
        signal_center = frequency - (channel_bandwidth / 2)    

        # Print out the results
        print("Frequency: %s\nModulation: %s\nChannel Bandwidth: %s\nSignal Center: %s" % 
        (frequency, modulation, channel_bandwidth, signal_center))