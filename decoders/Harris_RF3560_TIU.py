#!/usr/bin/env python

# TODO: Verify requirements for Harris RF-3560 TIU

import signal_framework as sf

class HarrisRF3560TIU(sf.BaseDecoder):

    def __init__(self):
        """Initialize decoder for Harris RF-3560 TIU"""
        # Set protocol for decoder
        self.protocol = 'Harris RF-3560 TIQ'

    def decode(self, signal_data):
        """Decode signal data and extract information from Harris RF-3560 TIU"""
        decoded_data = {}

        # TODO: Extract information from signal data using Harris RF-3560 TIU protocol

        return decoded_data