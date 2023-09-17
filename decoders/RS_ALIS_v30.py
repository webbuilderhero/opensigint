# TODO: Research how R&S ALIS v30 deals with RF signal intelligence

import numpy as np
import matplotlib.pyplot as plt

class RS_ALISv30_Decoder:
    """"
    Class to decode messages from R&S ALIS v30 RF signal intelligence
    """
    def __init__(self):
        # Initialize instance variables
        self.message_list = []
        self.message_dict = {}
     
    # Method to decode messages from R&S ALIS v30
    def decode(self, message):
        # Iterate over each character in message
        for char in message: 
            # Check if character is an alpha-numeric
            if char.isalpha() or char.isdigit(): 
                # Map the alphanumeric character to its binary representation
                binary_rep = self._map_char_to_bin(char)
                # Create a list of binary representation of every message character
                self.message_list.append(binary_rep) 
            else:
                # Map the other characters to its hexadecimal representation
                hex_rep = self._map_char_to_hex(char)
                # Create a list of hexadecimal representation of every message character
                self.message_list.append(hex_rep) 

        #Iterate over binary/hex list created
        for index,binary_hex_rep in enumerate(self.message_list): 
            # Generate the message from the symbols 
            if binary_hex_rep in self.message_dict:
                # Store the symbol number and its corresponding symbol in dictionary
                self.message_dict[index] = str(binary_hex_rep)
                
        # Return the decoded message from the dictionary
        return (str(self.message_dict.values()))
            
    # Method to map character to binary representation
    def _map_char_to_bin(self, char): 
        binary_rep = ord(char) 
        return "{0:04b}".format(binary_rep) 
    
    # Method to map character to hexadecimal representation
    def