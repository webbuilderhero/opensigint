#TODO: Figure out how to interpret the data coming from the RF signal. 

import pyaudio
import wave
import numpy
import math

#Function to convert audio frames to timestamps
def get_timestamps(audio):
    AUDIO_FRAME_LENGTH = 0.025 #Length of audio frames in seconds
    frames = audio.getnframes()
    rate = audio.getframerate()
    timestamp_inc = 0.0
    timestamps = []
    for f in range(0, frames):
        timestamps.append(timestamp_inc)
        timestamp_inc = timestamp_inc + (1 / rate) * AUDIO_FRAME_LENGTH

    return timestamps

#Function to decode Tandeme Selcall 
def decode_selcall(audio):
    #Get timestamp for each frame
    timestamps = get_timestamps(audio)

    #Identify the tone and determine its data content
    sample_width = audio.getsampwidth()
    NUM_CHANNELS = audio.getnchannels()
    audio_data = audio.readframes(audio.getnframes())
    audio_data = numpy.fromstring(audio_data, dtype=numpy.int16)

    all_tones = {
        'low': [697, 770, 852, 941],
        'high': [1209, 1336, 1477, 1633]
    }

    selcall_data = []
    for idx, timestamp in enumerate(timestamps):
        sample_index = int(math.floor(timestamp * audio.getframerate() * NUM_CHANNELS * sample_width))
        sample = int(round(audio_data[sample_index]))
        for tone, freqs in all_tones.items():
            for freq in freqs:
                if math.isclose(freq, sample):
                    selcall_data.append(tone)

    #Return data in selcall format
    selcall_data = ''.join(selcall_data)
    try:
        selcall_decoded = [int