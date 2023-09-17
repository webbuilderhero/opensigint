# TODO: Add support to decode Selcall audio signal

#import necessary modules
import numpy as np
import scipy.io.wavfile

# define a function to decode Selcall audio
def decodeSelcall(fileName):
    #open audio file using scipy
    sample_rate, sigData = scipy.io.wavfile.read(fileName)

    #apply inverse FFT to audio data
    inverseFFT = np.fft.ifft(sigData).real

    #identify start and stop symbols and isolate tone groups
    toneGroups = []
    startFound = False
    for i in range(len(inverseFFT)):
        if inverseFFT[i] > 0.3 and startFound == False:
            startFound = True
        
        if startFound == True:
            toneGroups.append(inverseFFT[i])
        if inverseFFT[i] < -0.3 and startFound == True:
            startFound = False
    
    #split tone groups into individual tones
    tones = []
    for group in toneGroups:
        if group > 0:
            tones.append(1)
        elif group < 0:
            tones.append(0)
    
    #convert tones to integer values
    binaryString = ''.join(str(x) for x in tones)
    intValue = int(binaryString,2)
    
    return intValue