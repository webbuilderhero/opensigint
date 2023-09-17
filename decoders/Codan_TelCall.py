"""
Decoder for Codan TelCall

TODO:
- Ask for help on how to plug into framework
"""

import gsm

def decode(input_data):
    """ Decode Codan TelCall using GSM """

    decoded_data = gsm.decode(input_data)

    return decoded_data

# Plug decoder into framework
def setup(module):
    module.add_decoder('Codan TelCall', decode)