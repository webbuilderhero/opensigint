#TODO:

#LPC-10e vocoder decode is not yet supported by our framework. 

#This script is intended to decode LPC-10e Vocoder-encoded messages from RF signals.

import struct

def decode_LPC_10e(data):
    """Decodes a LPC-10e Vocoder-encoded brush of data.
    
    Args:
        data (bytes): RF signal data to decode.
    
    Returns:
        decoded (string): Decoded message.
    """
    
    # Parse bitstream
    bitstream = []
    for byte in data:
         byte = format(byte, '8b')
         for bit in byte:
             bitstream.append(bit)
             
    # Create start and stop indices
    start_index = bitstream.index('1', 0)
    end_index = bitstream.index('1', start_index + 1)
             
    # Pull out encoded section
    encoded = bitstream[start_index : end_index + 1]
             
    # LPC-10e codewords consist of 10 bits
    codewords = [encoded[i * 10 : (i + 1) * 10] for i in range(len(encoded) // 10)]
    
    # Split bin into speech bit and parameters bit
    speech_bit = [cw[2:9] for cw in codewords]
    
    # Build the signals
    signals = []
    signal = 0
    for bit in speech_bit:
        signal = signal *2 
        if bit == '1':
            signal += 1
        else:
            pass
        signals.append(signal)
    
    # Interprete codewords
    decoded_bytes = ''
    for signal in signals:
        if signal <= 8:
            # Pause/Silence
            continue
        else:
            # Append byte from signals
            decoded_byte = struct.pack('b', signal)
            decoded_bytes += decoded_byte.decode('utf-8')
    
    decoded = decoded_bytes.