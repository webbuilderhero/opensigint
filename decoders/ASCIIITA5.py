#TODO: Research ITA5 to obtain additional information about the protocol 

import binascii

def ASCII_ITA5_Decoder(message):
    decoded_message = ""
    for i in range(0, len(message), 2):
        word = message[i:i + 2]
        word_in_hex = binascii.unhexlify(word).decode("utf-8") #translates the hexadecimal values of the two letters to ascii
        if word_in_hex == '$':
            decoded_message += ' '
        else: 
            letter_number = int(word_in_hex, 16)
            ascii_offset = 0 #ITA5 has a different starting letter to ascii characters and the offset measures the difference
            decoded_message_letter = chr(letter_number - ascii_offset)
            decoded_message += decoded_message_letter
    return decoded_message