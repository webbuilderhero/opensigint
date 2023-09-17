#!/usr/bin/python 

'''
TODO: Modify program to plug into framework
'''

# imports
import binascii

# get string to decode
print("Enter raw string to decode:")
raw_string = input()

# decode string
beacon_string = binascii.unhexlify(raw_string).decode('ascii')

# print decoded string
print("\nDecoded string:")
print(beacon_string)