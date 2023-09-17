#TODO: Replace this with codeword key
codeword =  ""

# This script is designed to decode the PRC64 signal from RF signals 
# for signal intelligence purposes
def PRC64_decoder(signal):
    # Initialize decoded string
    decoded_string = ""
    # loop through each element of the signal
    for val in signal: 
        if val in codeword: # Check whether current element matches codeword
            decoded_string = decoded_string + codeword[val] # Append the corresponding letter of the codeword to the string
        else:
            decoded_string = decoded_string + " " # If no match is found, add a space to the string
  
    return decoded_string # return decoded string 

if __name__ == "__main__":
    sig = [0,1,2,3,4,5] # Sample signal
    decoded_string = PRC64_decoder(sig) # Decode the sample signal
    print(decoded_string) # Print the decoded string