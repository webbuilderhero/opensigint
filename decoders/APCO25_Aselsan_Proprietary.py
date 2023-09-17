#TODO: Research signal modulation used in Aselsan Proprietary 

import collections 
import bitstring

# Decode Aselsan Proprietary signals 
def decode_APCO25_Aselsan_Proprietary(signal):
    
    #Perform DSP (Digital Signal Processing) on signal
    decimatedSignal = DSP(signal)
    
    #Extract signal properties
    signalProperties = extractSignalProperties(decimatedSignal)
    
    #Extract bitstream from signal
    bitstream = extractBitstream(decimatedSignal, signalProperties)

    #Create dictionary for decoding bitstream
    decodeDict = createDecodeDictionary()
 
    #Decode bitstream
    decoded = decodeBitstream(bitstream, decodeDict)

    #Apply noise reduction
    decoded = applyNoiseReduction(decoded)

    return decoded

#Perform DSP (Digital Signal Processing) on signal 
def DSP(signal):
 
    decimatedSignal = signal  #TODO: Add code specific to Aselsan Proprietary signal modulation here

    return decimatedSignal

#Extracts signal properties
def extractSignalProperties(signal):
    
    signalProperties = {}  #TODO: Add code specific to Aselsan Proprietary signal modulation here

    return signalProperties 

#Extracts bitstream from signal
def extractBitstream(decimatedSignal, signalProperties):
 
    bitstream = []  #TODO: Add code specific to Aselsan Proprietary signal modulation here
   
    return bitstream

#Create dictionary for decoding bitstream 
def createDecodeDictionary():
 
    decodeDict = {} #TODO: Add code specific to Aselsan Proprietary signal modulation here
 
    return decodeDict

#Decodes bitstream
def decodeBitstream(bitstream, decodeDict):

    decoded = collections.OrderedDict() #TODO: Add code specific to Aselsan Proprietary signal modulation here

    return decoded

#Applies