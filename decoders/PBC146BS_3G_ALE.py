# TODO: Determine what type of RF signal intelligence this decoder is for.

#!/usr/bin/env python

import re

def decode(string):
    # Remove all whitespace
    string = re.sub(r'\s+', '', string)

    # Parse the input string
    parts = re.findall(r"([A-Z\\-]+)([0-9]+)([A-Z]{2})", string)
    if len(parts) != 1:
        raise ValueError("Could not parse input string")

    # Get the parts as variables
    part1, part2, part3 = parts[0]

    # TODO: Add logic to decode the parts according to the type of RF signal intelligence

    # Print the resulting decoded values
    return {
        'part1': part1,
        'part2': part2,
        'part3': part3
    }

if __name__ == '__main__':
    decoded = decode('PBC-146BS 3G ALE')
    print(decoded)