import time

# TO-DO: add custom decoding definitions 

def decodeChirpCall(rawData):
    encodedMessage = ''
    
    byteData = bytearray(rawData)
    for byte in byteData: 
        byteval = format(byte, '08b')
        
        # Uncomment the decode definition for your language 
        # English
        #encodedMessage += chr(int(byteval[-2:] + byteval[-4:-2] + byteval[:-4], 2))
    
        # German
        #encodedMessage += chr(int(byteval[-3:] + byteval[-5:-3] + byteval[:-5], 2))

        # Spanish
        #encodedMessage += chr(int(byteval[-3:] + byteval[-5:-3] + byteval[:-5], 2))
    
    return encodedMessage

# TO-DO: integrate into main codebase 

if __name__ == "__main__":
    start_time = time.time()
    rawData = [1,154,50,4,3,3,3,6,3,3,3,3,3,3,3,3,3,5,2,0,254,3,0]
    decodedMessage = decodeChirpCall(rawData)
    print(decodedMessage)
    end_time = time.time()
    print("Execution time:", (end_time - start_time)*1000, "ms")