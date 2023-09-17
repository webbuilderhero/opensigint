# Decoder script for Mil-Std 188-110A/B/C/D serial

# specifies and defines each part of the Mil-Std 188-110A/B/C/D serial code
# data word is 144 bits long, divided into 18 octets of 8 bits each  
OCTET_0 = 0
OCTET_1 = 8
OCTET_2 = 16
OCTET_3 = 24
OCTET_4 = 32
OCTET_5 = 40
OCTET_6 = 48
OCTET_7 = 56
OCTET_8 = 64
OCTET_9 = 72
OCTET_10 = 80
OCTET_11 = 88
OCTET_12 = 96
OCTET_13 = 104
OCTET_14 = 112
OCTET_15 = 120
OCTET_16 = 128
OCTET_17 = 136

# specifies and defines each sub-division (bit range)
SOURCE_ADDR = (OCTET_0, OCTET_1) # 16 bits for source address  
DESTINATION_ADDR = (OCTET_2, OCTET_3) # 16 bits for destination address 

# TODO: figure out sub-divisions for OCTETS 4-17

# create function to convert Mil-Std 188-110A/B/C/D serial to proper address 
def mil_188_decoder (data):
    # converts binary data into decimal value 
    source_addr = int(data[SOURCE_ADDR[0]:SOURCE_ADDR[1]], 2) 
    destination_addr = int(data[DESTINATION_ADDR[0]:DESTINATION_ADDR[1]], 2)
    
    # TODO: Decode other sub-divisions and generate proper output 
    
    # output 
    output = {
        'source_addr': source_addr,
        'destination_addr': destination_addr
    }
    return output