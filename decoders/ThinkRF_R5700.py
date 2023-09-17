#TODO: Research the exact decoder needed for the ThinkRF R5700

#SigInt framework decoder for ThinkRF R5700

import sys

def thinkRfDecoder(file_in, file_out):
    """
    Decodes the specified input file for ThinkRF R5700 and outputs the decoded signal
    
    Parameters
    ----------
    file_in : str
        The filepath of the file containing the signal to decode
    file_out : str
        The filepath of the file that the decoded signal will be written to
    
    Returns
    -------
    None
    """
    
    # Open the input and output files for reading and writing
    fin = open(file_in, "rb")
    fout = open(file_out, "w")
    
    # Read the file bytes into a bytearray
    byteArr = bytearray(fin.read())
    
    # Loop over each byte in the array and decode it appropriately
    for byte in byteArr:
        # Byte coding specific to R5700 is implemented here
        # ...
        decodedByte = byte
        # ...
        
        # Write the decoded byte to the output file
        fout.write(decodedByte)
    
    # Close the opened files
    fin.close()
    fout.close()
    
# Main method for test running
if __name__ == "__main__":
    thinkRfDecoder(sys.argv[1], sys.argv[2])