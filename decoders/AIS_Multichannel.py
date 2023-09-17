# TODO: How to create input from RF signal

import numpy as np
import datetime

# This function takes an AIS Multichannel signal and decodes it into useful information
def decodeAISMultichannel(data):
	dataLength = len(data)
	
	# Validate channel lengths
	if (dataLength < 4) or (dataLength > 20):
		raise ValueError("Invalid length of AIS Multichannel signal")
	
	# Compute the UTC time when the signal was received
	now = datetime.datetime.utcnow()
	utcTime = now.strftime("%Y-%m-%d %H:%M:%S")
	
	# Get byte 0 - Channel ID and format
	channelId = data[0] & 0x1F
	formatCode = (data[0] & 0xE0) >> 5
	
	# Get all the data from the channel
	data = data[1:]
	data = np.fromstring(data, dtype=np.uint8)
	
	# Parse the data to extract SI, GPS, UTC, Position and Course
	si = data[0] & 0x3F
	gps = (data[0] & 0xC0) >> 6
	if len(data) >= 2:
		utc = int.from_bytes(data[1:3], byteorder='big')
	else:
		utc = 0
	if len(data) >= 6:
		position = data[3:5]
		course = data[5]
	else:
		position = [0, 0]
		course = 0
	
	return {
		"channelId": channelId,
		"formatCode": formatCode,
		"SI": si,
		"GPS": gps,
		"UTC": utc,
		"position": position,
		"course": course,
		"receiveTime": utcTime
	}