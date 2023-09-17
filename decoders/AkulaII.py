"""
TODO: Add Documentation
"""

import re

# Defines a decoder to decode the Akula-II RF signal intelligence format
def decodeAkulaII(sigint):
    # TODO: Extract valid Akula-II signature from the sigint
    
    # Initialize variables to store the Akula-II information
    payload = ""
    location = ""
    timestamp = ""
    
    # Initiate regular expression patterns for locating the individual fields of the signal
    payloadRE = re.compile(r"(?P<payload>(\w|\d|:)+?)\s")
    locationRE = re.compile(r"(?P<location>\w{2}:\d{3}.\d{2}:(?:[NESW]))\s")
    timestampRE = re.compile(r"(?P<timestamp>\d{2}:\d{2}:\d{2}\s?(?:AM|PM))")
    
    # Extract the payload from the sigint
    match = payloadRE.search(sigint)
    if match:
        payload = match.group("payload")
    
    # Extract the location from the sigint
    match = locationRE.search(sigint)
    if match:
        location = match.group("location")
    
    # Extract the timestamp from the sigint
    match = timestampRE.search(sigint)
    if match:
        timestamp = match.group("timestamp")
    
    # Return the extracted information
    return (payload, location, timestamp)