# TODO: Figure out what the code XD-D12B means

def decode(signal):
  
    # Split the signal into individual components, XD and D12B
    split_signal = signal.split("-")
    split_signal_x = split_signal[0]
    split_signal_d = split_signal[1]

    # Separate the components into type and data
    signal_type = split_signal_x[:2]
    signal_data = "+" + split_signal_d[1:]

    # Decoding the type
    if signal_type == "XD":
        result = "This is an emergency distress signal."
    elif signal_type == "SI":
        result = "This is an sensor input signal."
    elif signal_type == "RP":
        result = "This is an request for permission signal."
    elif signal_type == "SR":
        result = "This is an status report signal."

    # Decoding the data 
    # TODO: Figure out what the data means
    
    return result