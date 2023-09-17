# TODO: Get exact specs for decoding T-325/-353 DUDEK as there is no information available online to determine the specific algorithm used in this type of decoder 

import sys 

# Radio Frequency signal intelligence (SIGINT) decoder 
#  for T-325/-353 DUDEK encoded signals
def decodeT325_353Dudek(encodedSignal):
    # Define a lookup table of letters that correspond to each T-325/-353 DUDEK signal 
    appended_dict = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
        8: 'I',
        9: 'J',
        10: 'K',
        11: 'L',
        12: 'M',
        13: 'N',
        14: 'O',
        15: 'P',
        16: 'Q',
        17: 'R',
        18: 'S',
        19: 'T',
        20: 'U',
        21: 'V',
        22: 'W',
        23: 'X',
        24: 'Y',
        25: 'Z',
        26: '0',
        27: '1',
        28: '2',
        29: '3',
        30: '4',
        31: '5',
        32: '6',
        33: '7',
        34: '8',
        35: '9',
        36: '.',
        37: ',',
        38: "/",
        39: '-',
        40: ' ',
    }

    # Create a list/array that will store each letter as it's being decoded
    decoded_list = []

    for index, code in enumerate(encodedSignal):
        letter = appended_dict.get(code, -1)
        if letter == -1:
            print("Error: No valid T-325/-353 DUDEK signal found in list at index" + str