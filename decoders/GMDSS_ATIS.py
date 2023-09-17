"""
DECODER FOR GMDSS ATIS

#TODO: 
#1. Research and define GMDSS ATIS standards and parameters 
#2. Determine the format of the signals
#3. Find any necessary reference tables that the decoder will need

"""

import sys

class GmdssAtisDecoder:
    
    def __init__(self):
      # this is a placeholder until the feature of the GMDS ATIS is initialized 
        self.features = [] 

    def decode_signal(self, signal):
        """
        This function takes an input signal and decodes it according to the ATIS standards and parameters.
        """
        decoded = {}
        
        # loop through the features to decode each part of the signal
        for feat in self.features:
            
            try:
                # decode the signal according to the feature
                decoded[feat] = self.feat_decoder[feat](signal) 
            except:
                sys.stderr.write("Error decoding feature {}".format(feat))
                sys.stderr.write("Exiting decoder\n")
                sys.exit(1)
                
        return decoded 

    def register_feature(self, feat):
        """
        This function is used to register a feature that the decoder is able to decode. It takes the feature as an input and adds it to the feature list.
        """
        self.features.append(feat) 

    def register_feat_decoder(self, feat, decoder):
        """
        This function takes in a feature and a decoder and adds them to a dictionary which will be used 
        when we are decoding an incoming signal according to the features 
        """
        self.feat_decoder[feat] = decoder 
    
    def register_ref_table(self, name, table):
        """
        This function takes in a reference table name and its corresponding table values and adds it 
        to the reference tables dictionary. These tables will be used to decode the incoming signals.
        """
        self.ref_tables[name] = table 

if __name__