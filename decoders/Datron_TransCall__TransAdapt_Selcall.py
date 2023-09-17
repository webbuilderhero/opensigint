# TODO: Figure out how to access data in order to process it and extract meaningful information from it

import time

def datron_transcall_decoder(data):
    """
    Data should be in the format of a byte array. 
    Example: [0x01, 0x02, 0x3f, 0x4f, ...]

    This script will decode data that has been transmitted with
    the Datron TransCall and/or TransAdapt system.
    
    The output will be in the form of a list of tuples 
    containing the message type (e.g. station ID, frequency, etc.), 
    the station ID or frequency (if applicable), 
    and any metadata associated with the message (if applicable).
    """
    # TODO: Map data in data array to their specific functions
    # example: 0x01 = station ID, 0x02 = frequency, ...
    # Datron TransCall / TransAdapt system message types are as follows:
    # 0x01 = station ID
    # 0x02 = frequency
    # 0x03 = call request
    # 0x04 = call progress
    # 0x05 = call monitor

    station_id_flag = 0x01  # station id is first byte
    freq_flag = 0x02  # freq is second byte
    call_request_flag = 0x03  # call request is third byte
    call_progress_flag = 0x04  # call progress is fourth byte
    call_monitor_flag = 0x05  # call monitor is fifth byte

    output = []  # list to store output
    i = 0  # index placeholder

    while i < len(data):  # while not reached end of data
        if data[i] == station_id_flag:  # station id
            station_id = data[i + 1]  # next byte is the station id
            output.append(("station_id", station_id, None))  # append to output

        elif data[i] == freq_flag:  # frequency
            freq_val = data[i + 1]  # next byte is the frequncy
            output.append