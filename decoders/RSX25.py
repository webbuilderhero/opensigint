#TODO create a function that will receive an input string that represents an RSX.25 signal

import re 

def decode_signal(rsx_signal):
    """This function will decode an RSX.25 signal and output the
    decoded representation.
    
    Parameters:
    rsx_signal (str): RSX.25 signal to be decoded
    
    Returns:
    decoded_signal(str): Decoded representation of the RSX.25 signal
    """
    # Decode first set of numbers, separated by a period
    first_set_decoded = ""
    first_set = rsx_signal[0:3]
    first_decimal = int(first_set[0])
    first_one = int(first_set[1] / 2)
    first_two = int(first_set[2] % 10 + 10)
    first_set_decoded = str(first_decimal) + '.' + str(first_one) + str(first_two)

    # Decode second set of numbers, separated by a colon
    second_set_decoded = ""
    second_set = rsx_signal[4:7]
    second_decimal = int(second_set[0])
    second_one = int(second_set[1] / 2)
    second_two = int(second_set[2] % 10 + 10)
    second_set_decoded = str(second_decimal) + ':' + str(second_one) + str(second_two)

    # Decode third set of numbers, separated by a comma
    third_set_decoded = ""
    third_set = rsx_signal[8:11]
    third_decimal = int(third_set[0])
    third_one = int(third_set[1] / 2)
    third_two = int(third_set[2] % 10 + 10)
    third_set_decoded = str(third_decimal) + ',' + str(third_one) + str(third_two)

    # Output decoded string
    dec