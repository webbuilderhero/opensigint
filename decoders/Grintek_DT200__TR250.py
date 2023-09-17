"""
Decoder for Grintek DT200 / TR-250

TODO: Need to research and find out more about the protocol specifics
"""

#import necessary packages
import struct
import binascii
import array

#class for decoding message from Grintek devices
class GrintekDecoder:
    #constructor to initialize data
    def __init__(self):
        self.data_str = ''
        self.data_arr = []
    
    #Function to decode the given binary data string (data_str)
    def Decode(self, data_str):
        #convert binary data to hex representation
        self.data_str = binascii.hexlify(data_str).decode('utf-8')
        self.data_arr = array.array('H') #array of unsigned short
        
        #loop through data and store each 8 bits as a single byte
        for i in range(0, len(self.data_str), 8):
            #take 8 bits at a time
            byte = self.data_str[i : i + 8]
            #convert byte to unsigned short
            ushort = struct.unpack("<H", byte)[0]
            #append to data array
            self.data_arr.append(ushort)
        
        #TODO: Analyze data array for specific field/frame definitions
        #TODO: Process data array to extract relevant fields/values

#Test GrintekDecoder
def main():
    grintek_decoder = GrintekDecoder()
    grintek_decoder.Decode(b'\x7e\x01\x02\x03\x04\x05\x06\x07')
    print(grintek_decoder.data_arr)

if __name__ == '__main__':
    main()