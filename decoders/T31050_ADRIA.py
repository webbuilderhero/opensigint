# TODO add lines to set-up receiver frame, etc

""" 
This script decodes the T-310/50 ADRIA RF signal intelligence format. 
"""

import RF_Frame  # custom module for RF frame structure

# Define the frame bit rate
RATE = 2000

# Define the wave type (amplitude-modulated or frequency-modulated)
WAVE_TYPE = 'Pr'  # Pr for Pulse-reposition modulation 

# Establish the frame
ADRIA_FRAME = RF_Frame.RF_Frame(RATE, WAVE_TYPE)

# Setup the frame's headers, payloads, and trailer
HEADERS = []
PAYLOADS = []
TRAILER = []

ADRIA_FRAME.headers = HEADERS
ADRIA_FRAME.payloads = PAYLOADS
ADRIA_FRAME.trailer = TRAILER

# Define the signal sequence associated with this frame
SIGNAL_SEQUENCE = [
    'sync_seq1',
    'sync_seq2',
    'ERR',
    'CRC'
]

ADRIA_FRAME.signal_sequence = SIGNAL_SEQUENCE

# Set up the information to be sent and received
SEND_DATA = ''
RECV_DATA = ''

ADRIA_FRAME.send_data = SEND_DATA
ADRIA_FRAME.recv_data = RECV_DATA


# Function to decode the T-310/50 ADRIA signals
def decode_adria_signals(signals):
    """
    Decode the signals in the T-310/50 ADRIA signal intelligence format
    """

    # Get the contents of the frame
    frame_contents = ADRIA_FRAME.parse_frame(signals)

    # Parse each one of the ADRIA-specific headers/payloads/trailer
    headers = frame_contents["headers"]
    payloads = frame_contents["payloads"]
    trailer = frame_contents["trailer"]

    # Decode the payloads
    data = ADR