#TODO: Define constants such as shift amount, decryption key, etc

########  DECODER FOR FLEX  ########

#Importing python libraries and frameworks
import numpy as np 

#Defining constants
K = 6
SHIFT = 4
STR = "FLEX"

#Decrypt the string
def flex_decrypt():
    
    l = len(STR)
    out = ""
    for i in range(l): 
        x = (ord(STR[i]) - SHIFT*K) % 26
        out += chr(x + 97)
    
    return out

#Plug to the SIGINT framework 
def sigint_flex_decoder(encoded_string):
    
    decoded_string = ""
    for i in range(len(encoded_string)):
        decrypted_string = flex_dedrypt()
        decoded_string += decrypted_string
    
    return decoded_string