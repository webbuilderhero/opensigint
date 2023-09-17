#!/usr/bin/env python3
# TODO: Research ZVEI1 tonal system

import sys
import wave

def decode_zvei1(file_path):
""""Decoder for ZVEI1 tonal system

This decoder takes a file path to an audio file containing a signal
encoded using the ZVEI1 tonal system, and decodes the tones according
to the standard protocol.

It is assumed that the audio file is of the .wav file type, and is mono.

Args:
  file_path (str): File path to the audio file to be decoded

Returns:
   decoded (tuple): A tuple consisting of the decoded frequency and duration
"""

    with wave.open(file_path, 'rb') as f:
        sample_rate = f.getframerate()
        frame_length = f.getnframes()
        audio_data = f.readframes(frame_length)

    #Split the audio data into frequency,duration pairs
    frequency = []
    duration = []
    i = 0
    while(i < frame_length):
        #Get the frequency
        start_char = audio_data[i][0]
        end_char = audio_data[i+1][0]
        frequency.append(start_char + (end_char << 8))
        #Increment the counter
        i += 2
        #Get the duration
        start_char = audio_data[i][0]
        end_char = audio_data[i+1][0]
        duration.append(start_char  + (end_char << 8))
        #Increment the counter
        i += 2
    
    #Decode the tones according to the ZVEI1 protocol
    decoded = []
    for freq, dur in zip(frequency, duration):
        decoded_freq = decode_frequency(freq)
        decoded_dur = decode_duration(dur, sample_rate)
        decoded.append((decoded_freq, decoded_dur))

    return decoded


def decode_frequency(freq):
""""Decode