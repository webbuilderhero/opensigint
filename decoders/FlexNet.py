import numpy as np

#TODO: Research FlexNet protocol to determine necessary coding requirements

# Decoder for FlexNet
def flexnet_decoder(signal_input):
    # Initialize signal parameters
    signal_power = 0

    # Use numpy to translate signal frequencies to bits
    bits = np.where(signal_input == 1, 0, 1)

    # Output the decoded signal
    output_signal = []
    for bit in bits:
        output_signal.append(bit)
        signal_power += bit

    return (output_signal, signal_power)