#TODO: Research the QMAC Selcall broadcast protocol

import os
import sys
import argparse
from time import sleep

# defining command-line arguments
parser = argparse.ArgumentParser(description="Program to decode QMAC Selcall signals.")
parser.add_argument("-s", "--signal", type=str, required=True, help="Provide QMAC Selcall Signal to be decoded.")
args = parser.parse_args()

# setting the initial selcall frame and bit length values
SELCALL_FRAME_LENGTH = 10
SELCALL_BIT_LENGTH = 8

# lookup table to assign bits to selcall characters
selcall_table = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
}

# program body
def main():
    # declaring list variable to store selcall frames
    selcall_frames = []

    # extracting 10 frames from the signal
    for i in range(10):
        selcall_frames.append(args.signal[i*SELCALL_FRAME_LENGTH:(i+1)*SELCALL_FRAME_LENGTH])

    # decoding the selcall frames and storing them in a list
    decoded_selcall_frames = []
    for i in range(10):
        frame_bits = []
        for j in range(SELCALL_FRAME_LENGTH):
            frame_bits.append(selcall_table[int(selcall_frames[i][j])])
        decoded_selcall_frames.append(''.join(frame_bits))

    # printing out the decoded selcall frames
    for i in range(10):
        print(decoded_selcall_frames[i])


if __name__ == '__main__':
    main()