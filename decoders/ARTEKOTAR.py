"""

# TODO: Implement encryption/decryption methods

import math

def bunit(bin_str):
    """Convert a binary string into a byte"""
    byte_sum = 0
    for bit_str in bin_str:
        byte_sum += 2 ** int(bit_str)
    return byte_sum

def to_bin(text):
    """Convert a standard string of characters into binary string"""
    byte_str = ""
    for letter in text:
        byte_str += bin(ord(letter))[2:].zfill(8)
    return byte_str
    
def from_bin(bin_str):
    """Convert a binary string into a readable character string"""
    text = ""
    for i in range(math.ceil(len(bin_str) / 8)):
        text += chr(bunit(bin_str[i*8:(i*8+8)]))
    return text

def ARTEK_OTAR_encrypt(text):
    """Encrypts specified text using the ARTEK-OTAR encryption method"""
    #TODO

def ARTEK_OTAR_decrypt(encrypted_text):
    """Decrypts encrypted text using the ARTEK-OTAR encryption method"""
    #TODO
    
def ARTEK_OTAR_signal_decoder(signal):
    """Decodes a signal encrypted with the ARTEK-OTAR encryption method"""
    bin_signal = to_bin(signal)
    decrypted_signal = ARTEK_OTAR_decrypt(bin_signal)
    decoded_signal = from_bin(decrypted_signal)
    return decoded_signal