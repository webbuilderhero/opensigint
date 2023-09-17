# TODO: Figure out what protocol the WA2 Selcall uses
# TODO:6      Ensure that the script is interoperable with existing framework

import time

#Dictionary containing the decimal and binary representation of WA2 Selcall
selcall_dict = { 
    '0': '00', '1': '01', '2': '10', '3': '11'
}

#Function to decode incoming WA2 Selcall signal
def wa2_selcall_decoder(signal):
    #Split signal in to 4-bit chunks
    four_bit_chunks = [signal[i:i+4] for i in range(0, len(signal), 4)]
    #Convert 4-bit chunks into decimal value
    dec_vals = [int((x[0] + x[2]),2) for x in four_bit_chunks]
    #Map decimal values to corresponding characters
    out = list(map(lambda x: selcall_dict[str(x)], dec_vals))
    
    return ''.join(out)

#Function to continuously listen for WA2 Selcall signal
def wa2_listener():
    while True:
        signal = ''
        while (len(signal) != 32):
            #Listen for WA2 Selcall Signal
            signal = input("Enter WA2 Selcall Signal: ")
        #Decode WA2 Selcall signal
        decoded_signal = wa2_selcall_decoder(signal)
        print("Decoded Signal: {}".format(decoded_signal))

#starts program
wa2_listener()