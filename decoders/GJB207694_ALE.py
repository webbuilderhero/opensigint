"""
Decoder for GJB2076-94 ALE

TODO:
* Determine GJB2076-94 ALE protocol and specifics of what data is contained in the message

"""

import binascii 

class GJB2076_94_Decoder():
    """Decode GJB2076-94 ALE signal intelligence"""

    def __init__(self):
        pass

    def decode(self, packet):
        """Main decode function. 
        Input should be the packet string formatted according to GJB2076-94 ALE protocol.
        Returns a dictionary containing the decoded data.
        """
        payload = packet[:8] # extract payload from packet
        data = {
            'header': packet[0],
            'from_addr': packet[1:4],
            'to_addr': packet[4:7],
            'payload': binascii.unhexlify(payload),
            'crc': packet[8:11],
            'tail': packet[11]
        }
        return data

# testing
packet = "53XLMH00000000C8E4D"
decoder = GJB2076_94_Decoder()
data = decoder.decode(packet)
print(data)