import numpy as np
import matplotlib.pyplot as py

# TODO: Create a function to parse the ARQ-E3 data
def decode_ARQ_E3(data):
    # Initialize output variables
    output = []
    status = None
    # Loop over each byte of data
    for b in data:
        # Determine the status of the ARQ-E3 if it hasn't been set
        if not status:
            # if the top syndrome bit is 0 the transmitter is sending
            status = 0 if (b & 0x80 == 0) else 1
            # Set the status bit
            output.append(status)
            # Extract the remaining transmitter data
            output.append((b & 0x7F))
        else:
            # if the status was already set
            # the bottom 5 bits of the data are combined with the top 6 bits of the last byte to form 11 bits of data
            output.append((b & 0x3F))
            # Create the control byte decoding
            if status == 0:
                output.append('0' if (b & 0x40 == 0) else '1')
            else:
                output.append('0' if (b & 0x40 == 1) else '1')
            # Set the status bit for the next packet
            status = 0 if (b & 0x80 == 0) else 1
    # Return the decoded message
    return output
    
    
# Plot the decoded signal
def plot_decoded_signal(data):
    # Get the decoded message from the ARQ-E3
    decoded_data = decode_ARQ_E3(data)
    
    # Set up the pyplot and what data/axes to use
    x_values = np.arange(0, len(decoded_data))
    y_values = decoded_data
    py.plot(x_values, y_values, color='b')

    # Create the plot
    py.title('Decoded ARQ-E3 Signal')
    py.xlabel('Sample')
    py.ylabel('Signal')
    py.show()