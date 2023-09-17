"""
#TODO: import framework and get signal payload

import sys
import logging

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def wmbus_modes_decoder(payload):

    #Split payload into Mode S and Mode N
    mode_s_payload = payload[:9]
    mode_n_payload = payload[9:]

    #Decode Mode S
    #Mode S has a header, address and message
    mode_s_header = mode_s_payload[:3]
    mode_s_address = mode_s_payload[3:7]
    mode_s_message = mode_s_payload[7:9]

    #Decode Mode N
    #Mode N has a header, control field and information field
    mode_n_header = mode_n_payload[:3]
    mode_n_control_field = mode_n_payload[3:5]
    mode_n_information_field = mode_n_payload[5:]

    #produce a decoded output of the signal
    decoded_output = {
        "mode_s": {
            "header": mode_s_header,
            "address": mode_s_address,
            "message": mode_s_message
        },
        "mode_n": {
            "header": mode_n_header,
            "control_field": mode_n_control_field,
            "information_field": mode_n_information_field
        }
    }
    logging.info("Mode S and Mode N payloads decoded successfully")

    return decoded_output