# TODO:
# Make sure all 16 variants for AW-448 decoder are accounted for

import SigINT_Framework

#AW-448 DECODER

def AW_448_decoder(bitstream):
    #Check if length of bitstream is 448
    if len(bitstream) == 448:
        #Split bitstream into 16-bit chunks
        bit_chunks = map(''.join, zip(*[iter(bitstream)]*16))
        #Initialize variables for checksum, peak readings, and EEPROM
        checksum = 0
        peak_readings = []
        EEPROM = []
        #Iterate through each 16-bit chunk in bit_chunks
        for bi_chk in bit_chunks:
            #Check if chunk is for checksum
            if bi_chk[0] == '0':
                #Compute checksum
                for i in range(0, len(bi_chk), 4):
                    checksum += int(bi_chk[i+3], 2)*2**(i*4)
                #Subtract largest prime <= checksum
                checksum -= checksum % 311
            #Check if chunk is for peak readings
            elif bi_chk[0] == '1':
                #Add to peak readings
                peak_readings.append(int(bi_chk[1:],2))
            #Check if chunk is for EEPROM
            elif bi_chk[0] == '2':
                #Add to EEPROM
                EEPROM.append(int(bi_chk[1:],2))
        #Check if checksum is correct before returning final decoder output
        if checksum % 311 == 0:
            #Return decoder output as list
            return [peak_readings, EEPROM]
        #Return negative acknowledgement if checksum is incorrect
        else:
            return "NAK: Incorrect Checksum"
    #Return negative acknowledgement if bitstream length is not 448
    else:
        return "NAK: Incorrect Bitstream Length"

SigINT_Framework.set_decoder("AW-448", AW_