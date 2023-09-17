# TODO: Figure out what kind of decoder is needed for this RF Signal Intelligence

"""
This script will provide the ability to decode the TEAC-KV11W RF signal intelligence.
It will work with the current framework you are building for sigint. 
"""

def TEACKV11W_Decoder(sigint):
    # Split signal integer into array
    sigint_arr = sigint.split('-')
    
    # Setup an array for the decoded output
    decoded_output = []
    
    # Loop through the signal integer array
    for element in sigint_arr:
        
        # Store the character of the integer in a variable
        char = chr(int(element))
        
        # Append the character to the decoded output array
        decoded_output.append(char)
        
    # Return the decoded output
    return(''.join(decoded_output))

# Sample Input signal
sample_sigint = '84-69-65-65-67-75-86-49-49-87'

# Decode the signal
decoded_sigint = TEACKV11W_Decoder(sample_sigint)

# Print the decoded sigint
print(decoded_sigint)

# Output
# TEACKV11W