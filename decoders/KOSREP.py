# Decoder for KOSREP Signal Intelligence

"""
TODO:
- add logic for identifying the RF signal intelligence packets
- create data structure to store packet information
- implement decoding algorithm
"""

# imports
import datetime

# decoder class for KOSREP
class KOSREPDecoder():
    
    def __init__(self):
        self.packetLength = 0
        self.pktdata = []
        self.msgData = []
        
    # function to identify the KOSREP packet
    def identifyPacket(self, data):
        # check if the packet is of correct length
        l = len(data)
        if l == self.packetLength:
            # check for packet signature
            if (data[0] == 0xAA and data[1] == 0xBB):
                # packet is valid
                self.pktdata = data
        else:
            # wrong packet length
            self.pktdata = []
                    
    # function to decode the identified KOSREP packet
    def decodePacket(self):
        # check if we have a valid packet
        if len(self.pktdata) > 0:
            # packet is valid
            # decode further
            self.msgData.append( self.pktdata[2] & 0x7F )
            timestamp = datetime.datetime.fromtimestamp(self.pktdata[3])
            self.msgData.append(timestamp)
            # decode second half of packet
            msg = (self.pktdata[4] << 8) + self.pktdata[5]
            self.msgData.append(msg)
        else:
            self.msgData = []
            
    # function to get decoded message data
    def getMessage(self):
        return self.msgData