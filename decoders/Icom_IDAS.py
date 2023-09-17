"""Decoder for the Icom IDAS"""
import base64
import signal

#Todo: Add functionality to this script to connect with the other modules of your sigint framework. 

# Class to decode an Icom IDAS signal
class IcomIDASDecoder:

    def __init__(self):
        self.data = ""
        self.frameLength = 0
        self.encodedData = "" 

    # encode a signal into an Icom IDAS
    def encode(self, signal):
        self.data = signal
        self.frameLength = len(signal)
        self.encodedData = base64.b64encode(signal.encode('ascii'))

    # decode an Icom IDAS signal
    def decode(self):
        decodedData = base64.b64decode(self.encodedData)
        self.data = decodedData[:self.frameLength].decode('ascii')
        self.encodedData = ""

    # get the decoded signal
    def getDecodedData(self):
        return self.data

# Instatiate the decoder and connect to sigint framework
def main():
    icomIDASDecoder = IcomIDASDecoder()
    # connect to sigint framework
    #Todo: add code here to connect to the other modules of your sigint framework. 

if __name__ == '__main__':
    main()