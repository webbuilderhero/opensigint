#TODO: Research what Vyshka is

import binascii

def vyshka_decoder(signal):
    # Decode Vyshka signal
    decoded = ''
    for byte in signal:
        decoded += binascii.a2b_hex(byte)
    return decoded