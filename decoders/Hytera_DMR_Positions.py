"""
Hytera DMR Position Decoder
@author: __YourNameHere__

This script decodes data from Hytera DMR radios and position coordinate packets.

# TODO: Implement decoder
"""

# Import necessary libraries
import bitstring # For extracting data from the packets
import numpy as np # For manipulating and storing location data

# Convert hex strings into bitstrings 
def hex_to_bitstring(hex_string):
    return bin(int(hex_string, 16))[2:]

# Parse a single Hytera message packet
def parse_packet(hex_string):
    bitString = hex_to_bitstring(hex_string)
    data = bitstring.BitArray(bin=bitString).unpack(
        'uint:1,uint:1,uint:24,intle:4,intle:4,uintle:2, uint:3, uintle:3, uint:9, uint:7, uint:2, uint:4, intle:1, uint:3'
    )
    
    return data

# Extract GPS location from the parsed Hytera packet
def extract_location_data(packet):
    altitude = packet[4] # extract altitude from packet (metres)
    latitude_degrees = packet[2] // 600000 # extract latitude from packet (whole degrees) 
    latitude_remainder = packet[2] % 600000 # extract remaining decimal degrees
    latitude = latitude_degrees + (latitude_remainder * .00001) # combine whole and decimal degrees

    longitude_degrees = packet[3] // 600000 # extract longitude from packet (whole degrees)
    longitude_remainder = packet[3] % 600000 # extract remaining decimal degrees
    longitude = longitude_degrees + (longitude_remainder * .00001) # combine whole and decimal degrees

    location = np.array([latitude, longitude, altitude]) # store as numpy array

    return location

# Main function
def decode(hex_strings):
    locations = [] # stores locations
    for hex in hex_strings:
        try:
            packet = parse_