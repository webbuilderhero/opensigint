import logging

#TODO: research specific frequencies VHF ACARS uses and how to obtain them
#TODO: configure the logging library to save to a file

#create a class to hold the decoder
class acarsDecoder():

    #define __init__ to accept radio frequency data
    def __init__(self, radioFrequency):
        self.radioFrequency = radioFrequency

    #define main_decoder to decode the signal
    def main_decoder(self):
        '''This is the main decoder method. It accepts the radio frequency
        data and decodes the signal using VHF ACARS protocols
        '''

        #log the decoded signal
        logging.info('VHF ACARS signal decoded')

        #parse the data according to the VHF ACARS protocol
        decoded_data = self._parseData()
        return decoded_data

    #define parseData which will parse the data according to the VHF ACARS protocol
    def _parseData(self):
        '''This is a private method which parses the data according to 
        the VHF ACARS protocol
        '''

        #TODO: implement the VHF ACARS protocol to parse the data

        return parsed_data