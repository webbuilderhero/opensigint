#TODO: Add function to parse more specific settings for GL-5100 PSK (filter, crc, etc.)

#Decoder for GL-5100 PSK

import sys
import bitstring

def gl5100psk_decoder(data, settings):
    
    # Parse settings

    try:
        # Bit Rate
        bitrate = settings['bitrate']

        # Packet Length
        packet_length = settings['packet_length']

        # CRC
        crc_enabled = settings['crc_enabled']
    except KeyError:
        print('GL-5100 PSK settings not correctly configured')
        sys.exit(1)

    # Check if data has correct length
    if len(data) != packet_length * 8:
        print('Incorrect packet length. Expected ' + str(packet_length * 8) + ' bits, got ' + str(len(data)) + ' bits.')
        sys.exit(1)

    # Check CRC
    if crc_enabled:
        crc_data = bitstring.Bits(data[:-16])
        crc_calculated = bitstring.bits(crc_data.crc16()).int
        crc_received = int(data[-16:], 2)

        if crc_calculated != crc_received:
            print('CRC Check Failed!')
            sys.exit(1)

    # Remove CRC
    if crc_enabled:
        data = data[:-16]

    # Convert signal into bytes and parse data
    packet_data = bitstring.Bits(data).tobytes()

    return packet_data