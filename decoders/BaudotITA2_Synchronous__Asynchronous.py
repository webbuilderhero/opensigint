# TODO: Adapt script for your specific RF signal intelligence framework

# This script will take an input of a signal encoded by using the Baudot-ITA2 Synchronous / Asynchronous protocol
# and output it to standard ASCII characters.

#Define the Baudot-ITA2 Synchronous / Asynchronous character mapping
baudotITA2_Mapping = {
    0 : '\n',     #LF, Line Feed
    1 : '\t',     #Tab
    2 : ' ',      #Space
    10 : '\0',    #NUL
    11 : '0',
    12 : '1',
    13 : '2',
    14 : '3',
    15 : '4',
    16 : '5',
    17 : '6',
    18 : '7',
    19 : '8',
    20 : '9',
    21 : '.',
    22 : ',',
    23 : ':',
    24 : '?',
    25 : '\'',
    26 : '=',
    27 : '-',
    28 : '+',
    29 : '/',
    30 : '_',
    31 : '&',
    32 : 'A',
    33 : 'B',
    34 : 'C',
    35 : 'D',
    36 : 'E',
    37 : 'F',
    38 : 'G',
    39 : 'H',
    40 : 'I',
    41 : 'J',
    42 : 'K',
    43 : 'L',
    44 : 'M',
    45 : 'N',
    46 : 'O',
    47 : 'P',
    48 : 'Q',
    49 : 'R',
    50 : 'S',
    51 : 'T',
    52 : 'U',
    53 : 'V',
    54 : 'W',
    55 : 'X',
    56 : 'Y',
    57 : 'Z'
}

#This function takes a signal encoded with the Baudot-ITA2 Synchronous / Asynchronous protocol 
#and returns the standard ASCII characters
def