#!/usr/bin/env python3
# todo: need to figure out MIL-STD 188-141B ALE

# imports necessary packages
import bitstring

# Defining MIL-STD 188-141B ALE encoder/decoder class
class MIL_Std_188_141B_ALE_Decoder():
 
    def __init__(self):
        self.data_string = ""
        self.decoded_string = ""
        
    # Method to accept the binary string and decode it as per the MIL-Std 188-141B ALE
    # format
    def decode(self, data_string):
 
        # Set the class variable to the user input
        self.data_string = data_string
 
        # Convert it into a bitstring
        data_bitstring = bitstring.BitArray(data_string)
 
        # Read the first 6 bits as the data type as per the standard
        # [MSB] - [Data Description]
        #  00000 - Address field
        # 00001 - Information field
        # 00CAB - Extension field
 
        data_type_bits = data_bitstring[0:6]
 
        # Decode the data type
        data_type_decoded = self.decode_data_type(data_type_bits)
        
        # Depending on data type, call respective methods
        if data_type_decoded == "Address Field":
            self.decode_address_field(data_bitstring)
        elif data_type_decoded == "Information Field":
            self.decode_information_field(data_bitstring)
        elif data_type_decoded == "Extension Field":
            self.decode_extension_field(data_bitstring)
        else:
            print("Invalid data type received")
 
    # Method to decode data type bits
    def decode_data_type(self, data_type_bits):
        
        # List of data types
        # 00000 - Address field
        # 00001 - Information field
        # 00CAB - Extension field
 
        if data_type_bits == "