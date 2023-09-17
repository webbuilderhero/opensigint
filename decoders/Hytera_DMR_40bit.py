#TODO: Research needed on Hytera DMR 40-bit

#Import Libraries
import bitstring

#Create decoder class
class HyteraDMRDecoder():
    
    #Create constructor that takes in bitstring
    def __init__(self, bitstring):
        #Check if the bitstring is the correct bit lenght
        if not bitstring.len == 40:
            raise ValueError("Bit string must be 40-bits")
        else:
            #Set the bitstring in decoder
            self.bits = bitstring

    #Create decode method
    def decode(self):
        #Create decoded data object
        data = []
        #Read in the bits
        bits_arr = self.bitstring.bin #convert to binary
        #Loop through the bits to figure out decoding pattern
        for i in range(0, len(bits_arr), 8): #Loop 8 bits at a time
            #Append the decoded 8 bit character to the data list
            data.append(chr(int(bits_arr[i:i+8], 2))) #Decode 8 bits at a time with int class
        #Return all the decoded data
        return data