# TODO:
# Figure out a method for accessing weather data
# for the area specified in the "weather" argument
# of the decoder function.

# Decode a Facsimile FAX APT Weather RF signal
def decoder(signal):
   
    # Extract source from signal
    source = signal[:4]
    
    # Extract data length from signal
    data_len = signal[4:8]
    
    # Extract type of transmission from signal
    transmission_type = signal[8:14]

    # Extract type of weather from signal
    weather = signal[14:20]
    
    # Extract destination from signal
    destination = signal[20:]
    
    # Get weather data corresponding to the area
    # specified in the "weather" argument of the
    # decoder function 
    # TODO:

    # Construct decoded RF signal
    decoded_signal = {
        "source": source,
        "data_len": data_len,
        "transmission_type": transmission_type,
        "weather": weather,
        "destination": destination,
        "weather_data": 0, # TODO
    }
    
    return decoded_signal