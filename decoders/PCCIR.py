#!/usr/bin/env python
# TODO: Receive input for signal frequency and amplitude

import base64
import subprocess

def decode(signal):
  
    # Extract encrypted message from signal
    encoded_message = extract_message(signal)

    # Decode message with PCCIR
    decoded_message = decode_message(encoded_message)

    return decoded_message

def extract_message(signal):
    # TODO: extract the encoded message from the signal using the knowledge of signal frequency and amplitude
    return encoded_message

def decode_message(encoded_message):
    # Use PCCIR decoder to decode encrypted message
    response = subprocess.run(['pccir', encoded_message], stdout=subprocess.PIPE)

    # Capture the decoded message in bytes
    decoded_message = response.stdout

    # Convert decoded message from bytes to string
    decoded_message = decoded_message.decode("utf-8") 

    return decoded_message