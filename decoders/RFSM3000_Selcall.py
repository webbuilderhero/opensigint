# TODO: Improve print statements to make them more accurate
# TODO: Add ability to telnet into RFSM-3000 selcall

# Import libraries for decoding
import base64
import signal

# Define Function
def RFSM_3000SelcallDecoder():

    # Decoding step one 
    data_in = input("Input the data you wish to decode: ")
    data_out = base64.b64decode(data_in)

    # Decoding step two
    step2_out = ""
    for ch in data_out:
        step2_out += chr(ord(ch)-2)
    print("Data decoded step two: " + step2_out)

    # Final decoding step
    result = ""
    for ch in step2_out:
        result += chr(ord(ch)-1)
    print("Final decoding result: " + result)

# Handle interruption
def signal_handler(sig, frame):
    print ('\nYou pressed Ctrl+C')
    print("Program closing...")
    exit(0)

# Register signal
# If ctrl-c is pressed, call signal_handler() to close gracefully
signal.signal(signal.SIGINT, signal_handler)

# Run the decoder
RFSM_3000SelcallDecoder()