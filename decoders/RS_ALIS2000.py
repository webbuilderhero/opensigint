#TODO: research if the R&S ALIS-2000 has any external communications protocols 

#this is a basic script to decode signals from the R&S ALIS-2000
import struct

def signal_decode(data):
    '''
    Decodes signal data originating from the R&S ALIS-2000
    :param data: data from ALIS-2000
    :return decoded signal:
    '''
    # Create variables to store the decoded data
    rf_frequency = None
    signal_strength = None

    # Unpack the 32-bit data into the appropriate data types
    unpacked_data = struct.unpack('f f', data)

    # Unpack the rf_frequency first and then the signal_strength
    rf_frequency = unpacked_data[0]
    signal_strength = unpacked_data[1]

    # Create a dictionary for the response
    decoded_signal = {
        "rf_frequency": rf_frequency,
        "signal_strength": signal_strength
    }

    # Return the response
    return decoded_signal