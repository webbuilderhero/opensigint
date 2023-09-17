#TODO: Check for specific frequencies

import rfdecoder

class AT3004DDecoder:

    """This class implements decoder for AT-3004D novyy signal."""
    
    def __init__(self):
        self.decoder = rfdecoder.RFDecoder()
        self.model = "AT-3004D"

    def decode(self, signal):
        """Decode signal according to AT-3004D novyy signature"""

        decoded_signal = self.decoder.decode(signal)
        if decoded_signal.model == self.model:
            return decoded_signal
        else:
            return None