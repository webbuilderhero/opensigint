#TODO: Figure out the decoder specifics 

import radio

def ccir_1_decoder(data):
    """
    Decodes RF signals from CCIR-1 tonal mode into its corresponding signals
    
    Args:
        data (bytes): raw data from a rf signal

    Returns:
        str: decoded pure signal
    """
    signal = ""
    
    # Parse the data based on CCIR-1 tonal mode
    # In CCIR-1 tonal mode, 1 is represented by two hetrodyne sinusoidal waveforms and 0 is represented by a single waveform
    waveform_length = radio.get_waveform_length(data)
    for waveform in radio.iterate_over_data(data, waveform_length):
        # Find the waveform type, i.e., single or dual (for 0 and 1 respectively)
        waveform_type = radio.get_tone_waveform_type(waveform)
        
        # Translate the waveform type into a signal
        if waveform_type == "dual":
            signal += "1"
        else:
            signal += "0"

    # Return the decoded signal
    return signal