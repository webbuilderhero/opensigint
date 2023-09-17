'''
#TODO:
- Figure out how to access incoming RF data
- Determine what data EFR Telemetry provides
- Come up with the most efficient way to process incoming data
'''

import json
import numpy as np

TYPE = 'EFR Telemetry'

# Function to decode and format incoming EFR telemetry data
def decode_signal(data):
    decoded_data = json.loads(data)  # Decode incoming data

    # Fill in information for plotting graph
    x_axis_vals = np.array([data['timestamp']]) # Placeholder for x-axis values
    y_axis_vals = np.array([data['value']]) # Placeholder for y-axis values
    signal_type = TYPE  # Name of the signal (EFR Telemetry in this case)

    return x_axis_vals, y_axis_vals, signal_type  # Return necessary variables for plotting graph