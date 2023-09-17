# ToDo: Understand how to decode the signal 'XD-D9B1Data'

# imports
import re 

# Sigint Decoder
def decode_sigint(sigint): #this will take in the signal intelligence
    # 1. Break up the signal into smaller parts
    parts = re.findall(r'[A-Z]{2,}', sigint) #this will break the signal into two-letter or more than two-letter blocks 
    # 2. Decode each block
    decoded_list = [] #empty list to store decoded blocks
    for part in parts: #iterate thru the parts
        decoded_list.append(decode(part)) #add the decoded blocks to the list
    # 3. Reassemble the decoded parts
    decoded_sigint = ''.join(decoded_list) #join the decoded parts into a single string
    # 4. Print the decoded sigint
    print("Decoded Sigint: {}".format(decoded_sigint))

# Decoding helper function
def decode(data):
    #TODO: code to decode the string 'data'
    decoded = ""
    #loop through two letter blocks
    for i in range(0, len(data), 2):
        block = data[i:i+2] #pull out two letter block
        d1 = int(block[0], 16) #first character of the block
        d2 = int(block[1], 16) #second character of the block
        decoded += chr(d1*16 + d2) #convert two hexadecimal characters into one ASCII character
    return decoded