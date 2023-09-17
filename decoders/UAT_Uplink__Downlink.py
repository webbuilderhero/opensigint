#TODO: create new tables to store UAT uplink/downlink based paramters 

import pandas as pd

# define columns for uplink and downlink messages
Col_Uplink = ['MSG ID', 'Data 1', 'Data 2', 'Data 3', 'Data 4', 'Data 5', 'Data 6', 'Data 7']
Col_Downlink = ['MSG ID','Data 1', 'Data 2','Data 3', 'Data 4', 'Data 5', 'Data 6', 'Data 7', 'Data 8', 'Data 9']

# create empty dataframes to hold uplink and downlin messages 
uplink_frame = pd.DataFrame(columns=Col_Uplink)
downlink_frame = pd.DataFrame(columns=Col_Downlink)

# custom function to decode uplink and downlink messages
def decodeUAT(uplink_data, downlink_data):
    rx_uplink = 0
    rx_downlink = 0
    uplink_list = []
    downlink_list = []

    #split string and map data for uplink messages
    for uplink in uplink_data.replace(';', '').split(','):
        rx_uplink += 1
        uplink_list.append(uplink)
        
    #split string and map data for downlink messages
    for downlink in downlink_data.replace(';', '').split(','):
        rx_downlink += 1
        downlink_list.append(downlink)

    #adjust mapping for uplink messages
    if rx_uplink == 8:
        uplink_frame.loc[len(uplink_frame)] = uplink_list
     
    # adjust mapping for downlink messages  
    if rx_downlink == 9:
        downlink_frame.loc[len(downlink_frame)] = downlink_list

    return uplink_frame, downlink_frame 

# custom function to output data
def outputData(uplink_msg, downlink_msg):
    #output uplink message
    if uplink_