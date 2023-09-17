# TODO: research what BPSK63F is in relation to RF sigint
# TODO: further research how to decode these signals

import cmath

def bpsk63FDecoder(data):
    processedData = []
    
    for i in range(0, len(data), 8):
        sampleBlock = data[i:i+8]
        
        for x in range(0,8):
            if sampleBlock[x] >= 0:
                sampleBlock[x] = 1
            else:
                sampleBlock[x] = -1
        
        decoded = cmath.sqrt( sum( [ x**2 for x in sampleBlock ] ) )
        
        decoded /= 8
        
        vecDecoded = cmath.rect(1 , decoded)
        
        processedData.append(vecDecoded)
    
    return processedData