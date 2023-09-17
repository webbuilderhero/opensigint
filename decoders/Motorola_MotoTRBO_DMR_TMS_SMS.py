#!/usr/bin/env python3
""" Decode Motorola MotoTRBO DMR TMS SMS """

#TODO: Research necessary DMR_TMS and SMS protocols and figure out what type of data will be returned from each, and what type conversions may need to be applied 

import signal_intelligence_framework as sigint

def main(data_stream):
    """ Main decoding loop for Motorola MotoTRBO DMR TMS SMS. """
    
    # Set up base data for decoding
    DecodedData = []  # Create data holder
    
    #Pull necessary data from the data stream
    mototrbo_data = sigint.pull_data(data_stream, as_type='MotoTRBO')
    
    # Parse out the TMS data, if any
    if mototrbo_data.TMS:
        tms_data = mototrbo_data.TMS.value
	    #TODO: After further research, identify which format the TMS data is stored in and use an appropriate library or method to parse it 
        
        #TODO: Move on after parsing, by converting the data into a format that we can store in the DecodedData array 
	
    # Parse out the SMS data, if any 
    if mototrbo_data.SMS:
	    sms_data = mototrbo_data.SMS.value
	    #TODO: After further research, identify which format the SMS data is stored in and use an appropriate library or method to parse it 
        
        #TODO: Move on after parsing, by converting the data into a format that we can store in the DecodedData array
        	
    # Lastly, add the decoded data to the base data holder
    DecodedData.append(decoded_data)

    # Send DecodedData back to the framework
    sigint.return_data(DecodedData)

if __name__ == "__main__":  # Calls the main decoding function using the signal intelligence framework
    main(sigint.get_data_stream())