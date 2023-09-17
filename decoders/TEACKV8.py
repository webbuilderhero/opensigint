# TODO:  Determine frequency bands and protocols associated with TEAC-KV8

# Sigint processing pre-requisites 
from collections import defaultdict
import time

# Constants for frequency/protocols (determine experimentally)
MIN_FREQ = 400 # in MHz 
MAX_FREQ = 500 # in MHz 
PROTOCOLS = ["GMSK", "GFSK", "MSK"]

# Decoders associated with protocols 
DECODERS = {
    "GMSK": gmsk_decoder,
    "GFSK": gfsk_decoder,
    "MSK": msk_decoder
}


# Function for processing incoming TEAC-KV8 RF sigint 
def process_teac_kv8_sigint(data):

    decoded_data = defaultdict(list)

    # Get all the values from the data stream 
    freqs, protocols, data_streams = get_values_from_data_stream(data)
    
    # Iterate over protocols 
    for protocol, datastream in zip(protocols, data_streams):
        # Get the appropriate decoder for the protocol 
        decoder = DECODERS[protocol]
        decoded_data[protocol] = decoder(datastream) # decode 
    return decoded_data 


# Function for getting values from data streams 
def get_values_from_data_stream(data):
    # TODO: Implement function  
    pass