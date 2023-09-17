# TODO: Create script to enable additional functionality as needed.

import re

class SitorADecoder(object):
    '''Decoder for Sitor-A signal'''
    
    def __init__(self):
        self.encoding_table = {
            '0000': 'A',
            '0001': 'B',
            '0010': 'C',
            '0011': 'D',
            '0100': 'E',
            '0101': 'F',
            '0110': 'G',
            '0111': 'H',
            '1000': 'I',
            '1001': 'J',
            '1010': 'K',
            '1011': 'L',
            '1100': 'M',
            '1101': 'N',
            '1110': 'O',
            '1111': 'P'
        }
        
    def decode(self, signal):
        '''Decode a signal from Sitor-A'''
        # Split a signal into 4-bit characters
        signal_splits = [s for s in re.findall('.{4}', signal) if s != '']
        # Decode each 4-bit character into letter
        decoded_message = ''.join([self.decode_char(s) for s in signal_splits])
        # Return decoded message
        return decoded_message
    
    def decode_char(self, signal_char):
        '''Decode a 4-bit character into letter'''
        # Return decoded letter
        return self.encoding_table.get(signal_char, ' ')


# Test Code
if __name__ == "__main__":
    decoder = SitorADecoder()
    signal = '0111001011010010111100000100111'
    message = decoder.decode(signal)
    print(message) # Outputs HGFEDCP