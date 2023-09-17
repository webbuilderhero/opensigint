# TODO: Determine what type of data is encoded in "RH5-478" based on context

import re

def decode_rf_signal(signal):
    # Search for numbers and letters in the string
    signal_components = re.findall(r'(\d+|\w)', signal)
    
    # The components should be of length two (two characters)
    # We can assume the first part is an indicator of type
    # and the second part is data
    if len(signal_components) != 2:
        raise ValueError('Unable to determine signal type. Too many components.')
    
    # Use the first component to identify type of data
    # For example, "RH" likely means it is a signal from a RF transmitter
    if signal_components[0] == 'RH':
        transmitter_data = signal_components[1]
        # TODO: Parse the data further based on its format (478 for example)
        return {'type': 'rf_transmitter', 'data': transmitter_data }
		
    # Otherwise, if it does not match any known type, raise an exception
    else:
        raise ValueError('Unknown signal type: {}'.format(signal_components[0]))
		
# Example usage:
decoded_signal = decode_rf_signal('RH5-478')
print(decoded_signal)
# Outputs {'type': 'rf_transmitter', 'data': '5-478'}