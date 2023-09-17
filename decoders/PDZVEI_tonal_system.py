#TODO: Figure out incoming data format
#TODO: Figure out modules available to access the incoming data 

import pandas as pd
import numpy as np

def PDZVEI_decoder(data):
    df = pd.DataFrame(data)
    df['PDZVEI Num']= df['Data'].apply(get_PDZVEI_num)
    df['Tone'] = df['PDZVEI Num'].apply(convert_to_tone)
    return df

def get_PDZVEI_num(input_data):
    ''' 
    Takes a single value from the input_data and returns an integer corresponding to the PDZVEI numeral system.
    '''
    #TODO: Figure out formula for translating the incoming data   
    #to the PDZVEI numeral system
    
    return output_num

def convert_to_tone(pdzvei_num):
    ''' 
    Takes a single value from the output_num and returns an the corresponding tone as a string.
    '''
    #TODO: Figure out formula for converting the PDZVEI numeral 
    # system to the corresponding tone

    return tone