# TODO: research and determine further specs necessary to decode CCIR493-4 Proprietary 

import sys
 
# Decodes CCIR493-4 Proprietary signal intelligence
def Decoder(signal):
 
  decoded_signal = ''
  
   # CCIR493-4 Proprietary decoding code goes here
   
   return decoded_signal
 
# Main function that receives data and passes it to the decoder
def main():
  signal = sys.stdin.readline()
  
  decoded_signal = Decoder(signal)
  
  # Output the decoded message
  print(decoded_signal)
 
# Execute the main function
if __name__ == '__main__':
  main()