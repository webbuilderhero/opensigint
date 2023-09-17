#TODO: Include instructions in the script for users to plug in the decoder into their framework

# Decoder for TEAC-KV7 signal intelligence

#Import necessary modules
from time import time
import random

def decode_teac_kv7 (input):
    """
    This function takes an input RF signal in TEAC-KV7 format
    and decodes it into its component parts. 
    """
    #Break up input signal into four parts
    part_one = input[:4]
    part_two = input[4:8]
    part_three = input[8:12]
    part_four = input[12:]

    #Decode each part into its component parts
    part_one_info = decode_part_one(part_one)
    part_two_info = decode_part_two(part_two)
    part_three_info = decode_part_three(part_three)
    part_four_info = decode_part_four(part_four)

    #Combine pieces of decoded information
    msg = (part_one_info + " " + part_two_info + " " +
           part_three_info + " " + part_four_info)

    #Generate random ID for this message
    message_id = int(time() + random.randint(1,1000))

    #Generate decoded message object
    decoded = {
        "message_id": message_id,
        "message": msg
    }

    return decoded

def decode_part_one(part_one):
    """
    Decode part one of the signal into its components.
    """
    # Decode first two bits
    bit_1 = part_one[0]
    bit_2 = part_one[1]
    first_two_decoded_info = bit_1 + bit_2

    # Decode last two bits
    bit_3 = part_one[2]
    bit_4 = part_one[3]
    last_two_decoded_info = bit_3 + bit_4

    # Combine first and last two bits