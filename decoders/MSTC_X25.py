#TODO: Figure out signal format

#!/usr/bin/env python3

#Decoder for MSTC X.25
#RF Signal Intelligence

import sys
import re

#Function to parse incoming signals for X.25
def parse_x25_signal(raw_sig):
    #Regex to find valid signals
    x25_pattern = r'(33\.45(\X{7}\X{2}))?'
    #Regex to extract address from signal
    addr_pattern = r'\X{7}\X{2}'

    #Search signal for valid matches
    matches = re.search(x25_pattern, raw_sig)
    #If no valid matches, return nothing
    if not matches:
        return None
    else:
        #Store valid matches
        decoded_signal = matches.group(0)
        #Extract out address
        addr_match = re.search(addr_pattern, decoded_signal)
        if addr_match:
            address = addr_match.group(0)
            #Return address
            return address
        else:
            #Return empty string
            return ""

#Function to process signals and output viable received addresses
def process_signal(raw_sig):
    #Variable to hold decoded address
    decoded_addr = ""
    #Parse signal using parse_x25_signal
    decoded_addr = parse_x25_signal(raw_sig)
    #If address successfully decoded
    if decoded_addr:
        #Output address
        print("Received X.25 address: {}".format(decoded_addr))
    else:
        #Output failure message
        print("Failed to decode signal.")

#Main script
def main():
    #Check if signal provided
    if(len(sys.argv) > 1):
        #Process provided signal
        process_signal(sys.argv[1])
    else:
        #Output error message if no signal provided
        print("No signal provided.")

if __name__ == "__main__":
    main()