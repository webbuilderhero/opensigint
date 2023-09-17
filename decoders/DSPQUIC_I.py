# TODO: After first step (Flag and IQ Sampling), add more steps as needed

# Python script to decode DSP-QUIC signal
import radio
import coder

# Set up channel bandwidth, mode, and other parameters for the receiver
recv = radio.Receiver(mode=M_QUIC, bandwidth=20_kHz)

# Start sampling from the receiver 
samples, flag = recv.sample(sample_length=1024, offset=0)

# Perform quadrature demodulation 
iq_samples = coder.quadrature_demodulation(samples, flag)

# Decode DSP-QUIC signal
dsp_info = coder.decode_DSP_QUIC(iq_samples)

# Gather flock information
decoded_flocks = coder.get_flock_info(dsp_info)

# Print decoded information
print('Decoded DSP-QUIC Information: \n')
for flock in decoded_flocks:
    print('Flock Identifier: ' + flock)
    flock_info = decoded_flocks[flock]
    for key, value in flock_info.items():
        print('    ' + str(key) + ': ' + str(value))
    print()