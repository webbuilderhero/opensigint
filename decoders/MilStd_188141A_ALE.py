# TODO: any remaining parts of Mil-Std 188-141A ALE that aren't included in this decoder

import baseband  # library for signal processing
import sigint_framework  # custom library for sigint framework

class AleDecoder:
    # init function
    def __init__(self):
        self.active_list = []
        self.detected_mo_list = []

    # ALE recognition and message processing 
    def ale_recognition(self, signal):
        """
        This function takes in a signal and filters it for Mil-Std 188-141A ALE tones and 
        then processes the message. It returns the processed message if one is detected.
        """
        processed_message = None
        preamble_detect = False

        # filters
        signal = baseband.filter_children(signal)
        signal = baseband.high_pass_filter(signal)

        # ALE recognition
        message_chars = baseband.correlate_signal(signal, AleDecoder.ale_preamble)
        bit_stream = baseband.construct_frames(message_chars)

        # check for preamble
        if bit_stream[:8] == AleDecoder.ale_preamble:
            preamble_detect = True

        # if preamble is detected, process feilds of message
        if preamble_detect:
            first_char, second_char = baseband.decode_bits(bit_stream[8:16], AleDecoder.ale_alphabet)
            address = bit_stream[16:48]
            repeat_indicator = bit_stream[48:64]

            # if it's a new message, create it
            if repeat_indicator == 0:
                new_message = self.create_message(first_char, second_char, address)
                if new_message:
                    self.active_list.append(new_message)

            # if it's an existing message, update it
            else:
                for mo in self.active_list:
                    if mo.address_match(address):
                        mo.