"""

#TODO: Research RadioFrequency- Sigint techniques for URG-III HF Chat decoder

import radio
import signal

# Declare the names of the variables we'll be using later
frequency = 0   # The frequency of the signal
time = 0        # a 'time' variable which keeps track of when we start listening for signals
buffer_len = 0  # Length of the signal buffer

# Initialize Radio library
r = radio.Radio()

# This function is called when a signal is detected on the radio frequency
def signal_handler(data):
    # Check if the data in the buffer is on the same frequence
    # that we're listening for
    if data['frequency'] == frequency:
        # Decode the data
        decoded_data = radio.decode(data['raw'], data['buffer_len'])
        
        # Check if the data is a valid URG-VII HF Chat message
        if decoded_data.startswith('URG-VII HF'):
            # Print out/return the decoded data
            print(decoded_data)
            
# Start listening for signals on the frequency
r.listen(frequency, signal_handler, time, buffer_len)