# This script decodes Invelco MD-571-A Signal Intelligence 

# TODO - Flesh out logic for decoding algorithm

##### Pre-requisites #####
import binascii # used for byte to Hex conversion 
import struct # used to convert hex representations of data into their binary equivalents

# create a mapping of subtype (1st Byte) to type
invelco_code_map = {
    '00': 'NULL',
    '01': 'CALL',
    '02': 'ACK',
    '03': 'CHECK',
    '04': 'BAND CHANGE',
    '05': 'DISCONNECT',
    '06': 'VERIFY',
    '07': 'HELLO',
    '08': 'RESET',
    '09': 'STATUS'
}

##### Functions #####

# function for decoding main type of communication
def decode_invelco_type(subtype_hex):
    subtype_bin = binascii.unhexlify(subtype_hex)
    subtype = struct.unpack('<B',subtype_bin)[0]
    try:
        communication_type = invelco_code_map[str(subtype)]
    except:
        communication_type = 'Unknown Type'

    return communication_type

##### Main #####
# take in data in bytes from decoder
# convert the data into Hex
data_BytesObj = b'\x06\x00\x00\x00\xFF\xFF'
data_Hex = binascii.hexlify(data_BytesObj)

# extract 1st byte which represents the communication type for Invelco
communication_type_hex = data_Hex[0:2] # return '00'

# decode that byte using our decode_invelco_type function
communication_type = decode_invelco_type(communication_type_hex) # return 'VERIFY'

# Output the type of communication
print('Communication Type: ', communication_type) # print 'VERIFY'