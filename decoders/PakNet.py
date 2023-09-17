#todo: Inputs, scope, architecture, etc

import time

# Define the decoder class 
class PakNetDecoder: 

    # Initializer / Instance Attributes
    def __init__(self, scope):
        self.scope = scope

    # Instance Method
    def decode_message(self): 
        print("Decoding PakNet message...")
        time.sleep(2)
        print("Message decoded.")
        print("")

    # Instance Method
    def decode_signal(self):
        print("Decoding RF Signal...")
        time.sleep(2)
        print("Signal decoded.")
        print("")

# Define main function
def main():
    # Initialize PakNet Decoder
    paknet_decoder = PakNetDecoder("Signal Intelligence")

    # Decode Message 
    paknet_decoder.decode_message()

    # Decode Signal
    paknet_decoder.decode_signal()

# Execute the Decoding script
if __name__== "__main__":
  main()