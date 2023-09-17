# ToDo: Research to determine exactly how DMR Mode 1, Mode 2 and Mode 3 of Tier 1 should be decoded 

import os
import logging

logging.basicConfig(level=logging.DEBUG)

class DMRSignalDecoder(object):
    def __init__(self):
        self.symbol_length = None  # ToDo: Determine length of one symbol for DMR Mode 1, Mode2 and Mode3 Tier 1
        self.preamble_length = None  # ToDo: Determine length of preamble for DMR Mode 1, Mode2 and Mode3 Tier 1
        self.check_sum_length = None  # ToDo: Determine length of check_sum for DMR Mode 1, Mode2 and Mode3 Tier 1
        self.packet_length = None  # ToDo: Determine length of packet for DMR Mode 1, Mode2 and Mode3 Tier 1
        
    def decode_packet(self, packet):
        """
        Decodes DMR Mode 1, Mode 2 and Mode 3 Tier 1 packets
        :param packet: Byte array
        :return: dictionary object containing information from packet
        """
        packet_dict = {}
        
        # ToDo:Figure out the specific parts of the packet that we need to decode for DMR Mode 1, Mode 2 and Mode 3 Tier 1
        # ToDo:Research the specific details of decoding DMR Mode 1, Mode 2 and Mode 3 Tier 1 and put it within this method
        
        return packet_dict