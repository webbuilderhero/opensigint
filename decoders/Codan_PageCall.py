"""
Decoder for Codan PageCall
"""

#todo: import any necessary libraries
import pandas as pd

#todo: define any global variables here
protocol_name = 'Codan PageCall'

def decode(dataframe):
    """
    Description: Decoder for Codan PageCall
    Inputs: 
        dataframe - Dataframe containing signals data of Codan PageCall
    Outputs:
        Dataframe containing decoded signals
    """
    #todo: implement the decoder
    decoded_signals = pd.DataFrame()
    
    #todo: get the signals requiring decoding
    signals_to_decode = dataframe.loc[dataframe['Protocol'] == protocol_name]
    if signals_to_decode.empty:
        return decoded_signals

    #todo: parse and decode the signals
    #todo: add the decoded signals to the output dataframe
    for idx, row in signals_to_decode.iterrows():
        #todo: parse and decode the signal in the row
        decoded = _decode_signal(row)
        decoded_signals = decoded_signals.append(decoded, ignore_index=True)
    return decoded_signals

def _decode_signal(signal):
    """
    Description: Helper function to decode a signal
    Inputs: 
        signal - a single signal data as a pd.Series
    Outputs:
        decoded - a decoded signal as a pd.Series
    """
    #todo: Implement decoding logic for Codan PagCall
    decoded = pd.Series()

    #todo: extract values from signal

    decoded['Type'] = 'PageCall'
    decoded['Message'] = signal['Raw Data']

    #todo: return the decoded signal
    return decoded