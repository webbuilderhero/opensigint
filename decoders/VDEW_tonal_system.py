# TODO: need to develop signal reading/processing algorithm

import numpy as np

# Codebook for VDEW Tones
codebook = {
    # tone 1
    0 : [2300, 2500, 2700],
    # tone 2
    1 : [2900, 3100, 3300],
    # tone 3
    2 : [3500, 3700, 3900],
    # tone 4
    3 : [4100, 4300, 4500]
    }

def decode_VDEWTones(inputSignal):
    outputSignal = []
    # Iterate through signal
    for signal in inputSignal:
        # Check each tone in codebook
        for tone in codebook:
            if np.all(np.isin(signal, codebook[tone])):
                outputSignal.append(tone)
                break # only activate one tone at a time
    return outputSignal

if __name__ == '__main__':
    # three tones as a test signal
    testSignal = [[2300,2500,2700],[2900,3100,3300],[4100,4300,4500]]
    print(decode_VDEWTones(testSignal)) # [0, 1, 3]