#TODO: Research methodology for determining signal source and data bits

#!/usr/bin/env python3
import math

def decoder_EIA(input_data):
    """A decoder for converting EIA (Electronic Industries Association) signal data to recognizable data. 
    
    Args:
        input_data (int) : An input signal data in EIA format
    
    Returns:
        output_data (string): A decoded string of the data
    
    """
    try:
        #Calculate the symbol rate, which is the inverse of the bit period
        #Bit period for EIA signals is 3/16th of a second (roughly 18.75 milliseconds)
        symbol_rate = 1/(3/16*1000)
        
        #Calculate length of input and create a list of elements
        length = len(input_data)
        data_list = list(input_data)

        #initialize variable to store output
        output_data = ""

        #loop through the list of elements and map EIA values to integer values
        for bit in data_list:
            if bit == "P":
                output_data += '0' 
            elif bit == "N":
                output_data += '1'
            elif bit == "I":
                output_data += '2'
            elif bit == "S":
                output_data += '3'
            else:
                output_data += '4' 

        return output_data, symbol_rate
	
    except:
        #If any errors occur, raise an exception
        raise Exception("Error in decoding EIA signal, check input parameters")