"""
#ToDo: try to check if any specific encoding is used and implement that.

import os

def T31051_decoder(data):
    
    output_data = ""

    #The T-310/51 SAGA is an AES 256 Encryption system
    #We need to decrypt the data with the key
    key = os.environ.get('T310_KEY') #Get Environment Variable with key
    if key is not None:
        from Crypto.Cipher import AES
        cipher = AES.new(key, AES.MODE_CBC)
        output_data = cipher.decrypt(data)
    
    return output_data