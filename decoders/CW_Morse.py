# TODO: Make sure that the code is able to identify the difference between a letter and a number in the message/cipher

def decodeMorse(input_string):
    '''
    Takes a morse code string and returns the plaintext. 
    '''

    # Reference dictionary for morse code - letters
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',  'C':'-.-.', 'D':'-..', 'E':'.',  'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 
    'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', 
    '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', 
    '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-'
    } 

    # References dictionary for morse code - numbers
    MORSE_CODE_NUM = { '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
    '8':'---..', '9':'----.', '0':'-----'         
    } 
    
    # Initialize the decoded plaintext
    decoded_message = ""