#TODO: Research MIL-STD to ensure accuracy for decoding

# Imports 
from bitstring import BitArray

# Message decoding variables
DATA_RATE = "4xQPSK"
WORD_COUNT = 6         
MICRO_PER_WORD = 836    
TOTAL_MICROSECONDS = WORD_COUNT * MICRO_PER_WORD

def decode_message(encoded_message):
    """Performs MIL-STD 188-110A APP B decoding for RF signal intelligence"""

    # Create a bit array from encoded message
    bit_array = BitArray(hex=encoded_message) 

    # Check to make sure message is long enough
    if ((TOTAL_MICROSECONDS / 8) > len(bit_array)):
        return "The message is too short."

    # Check to discretize bit array into 8 bits per symbol
    if (DATA_RATE == "4xQPSK"):
        if (bit_array.length % 8 != 0):
            bit_array.append((8 - (bit_array.length % 8)) * '0b0')
            
    # Split bit array into 6 words (836 bits each)
    total_words = bit_array.length // 836
    words = [BitArray(length=836) for word in range(total_words)]
    index = 0
    for word in range(total_words):
        words[word] = bit_array[index:index + WORD_COUNT * 8]
        index += WORD_COUNT * 8

    # Decode words according to MIL-STD 188-110A APP B
    decoded_words = bit_array_to_int(words)
    return decoded_words

def bit_array_to_int(words):
    """Converts an array of bit arrays to an array of int"""
    decoded = []
    for word in words:
        decoded.append(int(word.bin, 2))
    return decoded