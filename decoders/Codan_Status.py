# TODO: Add Sigint Framework 

# Decoder for Codan Status

# Import necessary modules
import socket
import time

# Generic constants 
TIMEOUT = 5

# Establish connection to port 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.settimeout(TIMEOUT)

# Begin listening for incoming signals from port 
while True:

    # Get raw data from port 
	sock.listen(1)
	conn, addr = sock.accept()
	data = conn.recv(1024)

	# Parse and decode incoming signal 
	cod = data.split(",")
  	timestamp = cod[0]
	data = cod[1:]

	# Save data into array to be decoded
	decoded_data = []
	for byte in data:
		decoded_data.append(int(byte,16))
  
	# If the first byte of the data is 0x02
  # then the next two bytes are the status of the 
	# Codan signal 
	if decoded_data[0] == 0x02:
  		status = str(decoded_data[1]) + str(decoded_data[2])

		# Read the byte values of status and map to 
		# Codan values
		if status == "01":
    		status_string = "Power On Reset | Initializing"
		elif status == "02":
    		status_string = "Operating and transmitting"
		elif status == "04":
    		status_string = "Power on reset | Uninitialized"
  	print (timestamp + " : " + status_string)
	conn.close()
sock.close()