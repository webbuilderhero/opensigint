#TODO: Check for unique ID for VIP-117M2 Long/Short

import base64

#decoding function
def decode(s):
    try:
        #decode string using base64 code
        decoded_str = base64.b64decode(s)
        #return the decoded string
        return decoded_str
    
    #if error occurs during decoding, return 0
    except:
        return 0

#decode PIRS PEARCE VIP-117M2
pirs_pearce = decode("PIRS PEARCE VIP-117M2")
#check if unique ID is present
long_short = 0
if ('Long/Short' in str(pirs_pearce)) is True:
    long_short = 1

#print if unique ID is present
if long_short == 1:
    print('Unique ID found! PIRS PEARCE VIP-117M2 Long/Short is decoded.')
elif long_short == 0:
    print('Unique ID not found. Check your data.')