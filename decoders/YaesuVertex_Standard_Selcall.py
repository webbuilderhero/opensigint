# TODO: Provide implementation specific to RF signal intelligence

# Decoding Yaesu/Vertex Standard Selcall
import sys

def selcall_decode(bits):
    """
    Decodes bits into Yaesu/Vertex Standard Selcall information

    :param bits: The bit sequence of the Selcall
    :returns: A dictionary with the decoded information
    """

    # The number of valid bits for Selcall
    BIT_LEN = 32

    # Check the length of the bit sequence
    if len(bits) != BIT_LEN:
        raise ValueError('Invalid bit length! Expected {}, got {}'.format(BIT_LEN, len(bits)))

    # Create the variable to return
    ret = {
        'form': '',
        'function': '',
        'ID1': '',
        'ID2': '',
    }

    # Decode the form
    if bits[0:2] == '11':
        ret['form']  = 'AFSK'
    elif bits[0:2] == '00':
        ret['form']  = 'FSK'
    elif bits[0:2] == '01':
        ret['form']  = 'FSK'
    elif bits[0:2] == '10':
        ret['form']  = 'AFSK'

    # Decode the function
    if bits[2:4] == '01':
        ret['function']  = 'Selective Call'
    elif bits[2:4] == '11':
        ret['function']  = 'Voice Call'
    elif bits[2:4] == '00':
        ret['function']  = 'Steady Tone Call'
    elif bits[2:4] == '10':
        ret['function']  = 'Data Call'

    # Decode the ID1
    ret['ID1']  = int(bits[6:18], 2)

    # Decode the ID2
    ret['ID2']  = int(bits[18:30], 2)
		
    return ret

if __name__ == '__main