# Sigint decoder for PIRS PEARCE VIP-117M3 Short/ARQ

# TODO - Add more logic/checks per the specific RF signal intelligence protocol

import struct

MARK_1 = 0xC0
MARK_2 = 0xFC

def decodePIRSPearceVIP117M3ShortARQ(data) :
    decoded = {}
    if len(data) == 5 and data[0] == MARK_1 and data[1] == MARK_2 :
        decoded['mark1']  = data[0]
        decoded['mark2'] = data[1]
        decoded['type']  = data[2]
        decoded['data_id'] = data[3]
        decoded['checksum'] = data[4]

        # calculate expected checksum
        sum = decoded['type'] + decoded['data_id']
        expected_checksum = sum & 0xFF

        # compare expected and observed checksums
        if expected_checksum != decoded['checksum'] :
            raise ValueError('Checksums do not match - expected %d, got %d' %
                            (expected_checksum, decoded['checksum']))

    else :
        raise ValueError('Incorrect packet length')

    return decoded