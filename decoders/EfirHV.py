"""
Decoder script for Efir-HV signal intelligence

TODO:
- Modify code for broadcast configuration and low latency
- Add capability to decode encrypted signals

"""
import radio
import binascii

def efir_hv_decoder():
    # Establish radio connection
    radio_connection = radio.Radio()

    # Setup parameters for radio connection
    data_rate = radio_connection.set_data_rate(250)
    modulation_type = radio_connection.set_modulation('GFSK_1_2')

    # Checks to make sure parameters are set correctly
    if data_rate and modulation_type:
        # Setup radio receiver
        radio_receiver = radio.Radio_receiver(radio_connection)
    
        # Continuously loop and receive signals
        while True:
            # Retrieve signal data
            signal_data = radio_receiver.receive_signal_data()
            if signal_data:
                # Retrieve signal bytes
                signal_bytes = binascii.hexlify(signal_data)
                # Translate signal bytes
                decoded_signal = decode_signal_bytes(signal_bytes)
                # Return decoded signal
                return decoded_signal

    else:
        print("Could not set required data rate and/or modulation type for radio connection.")

def decode_signal_bytes(signal_bytes):
    # Decode signal based on protocol/encoding used    
    # INSERT DECODING LOGIC HERE

    # Return decoded signal
    return decoded_signal