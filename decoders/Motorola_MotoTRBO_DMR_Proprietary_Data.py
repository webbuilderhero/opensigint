#Todo: Refine decoding process (ie: figure out the exact decoding type) 

import bitstring

# Class to handle decoding of Motorola MotoTRBO DMR Proprietary Data
class MotorolaMotoTRBODmrDecoder():
    def __init__(self):
        # specific information used by decode function
        self.reg_values = {
            "SID": 0,
            "Rewrite Table": 1
        }

    # function that takes in a binary string and infers Motorola MotoTRBO DMR Proprietary Data
    def decode(self, signal):
        # Conversion of the signal data from a bitstring to a list
        bit_list = bitstring.Bits(signal).tolist()
        decode_list = []

        if bit_list[0] == 0:
            # Decoding of Service Identifier (SID)
            sid = self.reg_values[bit_list[1]+bit_list[2]]
            decode_list.append(("SID", sid))

        # Decoding Rewrite Table
        # Calculate Rewrite Table index position based on SID
        # placement in the bit string
        if 23 <= bit_list[1]+bit_list[2] <= 28:
            rewrite_table_idx = 8
        else:
            rewrite_table_idx = 20

        # Calculate Rewrite Table data based on the bit string
        rewrite_table_data_list = []
        for i in range(rewrite_table_idx, rewrite_table_idx+8):
            rewrite_table_data_list.append(bit_list[i])

        # Append the Rewrite Table data to the decode list
        decode_list.append(("Rewrite Table", rewrite_table_data_list))

        return decode_list