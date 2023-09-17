import sys

#Todo: Research CCIR-7 Tonal System

def decodeCCIR7(stream):
    # Initialize empty byte array
    data = bytearray()

    # Loop through and extract each byte
    for bit in stream:
        # Add the bit to the byte
        data[-1] = (data[-1] << 1) | bit
        
        # If the 8th bit is set then move on to the next byte
        if data[-1] & (1 << 7):
            data.append(0)
        
    # Return the decoded data
    return data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decodeCCIR7.py [CCIR-7 Stream]")
        sys.exit(1)

    stream = sys.argv[1] # Get the input CCIR-7 stream
    data = decodeCCIR7(stream) # Decode the stream using decodeCCIR7

    print("Decoded Data:", data) # Print out the decoded data