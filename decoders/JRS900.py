#TODO: Find out the specific protocol and format of JRS-900

import json

class JRS_900_Decoder:
    #JRS-900 Decoder

    def decode(data):
        """
        Function to decode the JRS-900 signal
        Input:
            data (byte array): the raw signal data
        Output:
            json-formatted data
        """

        #TODO: write code to decode JRS-900 data

        #Assuming the protocol is a standard one
        words=[data[i:i+4] for i in range(0, len(data), 4)]
        decimalValues=[int(word[::-1],2) for word in words]
        #TODO: map the decimal values with some meaningful values
        #Considering a simple mapping of 1=true, 0=false
        booleanValues=[True if val else False for val in decimalValues]
        
        return json.dumps(booleanValues)