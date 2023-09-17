#TODO understand meaning behind 1200bd/9600bd

#PYTHON DECODER SCRIPT
import json

#This function will decode the 1200bd/9600bd signal.
def decoder(packet):
  #TODO determine which type of Baud rate the signal is using 
  
  #Set default baud rate 
  baud_rate = 1200
  
  #Check if baud rate is 9600
  if (packet == 9600):
    baud_rate = 9600
  
  #Decode the packet
  decoded = ""
  
  #TODO: Determine how to best decode the packet based on the baud rate 
  
  return decoded
 
#Save the decoded packet to a file
def save_packet(packet):
  #TODO write code to save the decoded packet to a file 
  
  with open("packet.json","w") as outfile:
    json.dump(packet, outfile)
  
  return "Packet Saved"

#Usage example
packet = '1200bd/9600bd'

#Decode the packet
decoded_packet = decoder(packet)

#Save the decoded packet
save_packet(decoded_packet)