#TODO: Further research to understand the format of signal and type of data being collected

import struct

#RT-2001 Decoder
def rt_2001_decoder(data):
    """
    This is a decoder for the Tadiran RT-2001 Radio Reciever
    It parses the raw data from the signal to variables 
    and returns meaningful information in a dictionary format
    """
    # Unpacking the raw data
    raw_data = [i for i in data]
    data_radix = int(raw_data[0]/10**2)
    data_ref = int(raw_data[1])
    data_value = int(raw_data[2])
    data_type =  int(raw_data[3]/10**4)

    # Dictionary of different types of data
    # Corresponding to the data_type
    type_dict = {
        1: "Battery Level ",
        2: "Temperature ",
        3: "Wind Speed ",
        4: "Pressure ",
        5: " Rainfall ",
        6: "Humidity ",
        7: "Soil Temperature" 
    }

    # Creating Dictionary to return
    info = {
        'Radix': data_radix,
        'Reference': data_ref,
        'Value': data_value,
        'Type': type_dict[data_type]
    }

    return info