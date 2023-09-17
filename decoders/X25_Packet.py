import rf_signal_intelligence as rf
import x25.packet_decoder as x25_pkt

#todo: put in try catch statement

#returns a dictionary of decoded packet info
def decode_x25_packet(packet_data):
    # decode X.25 packet
    decoded_packet_data = x25_pkt.decodePacket(packet_data)

    # organize the decoded packet data into a dictionary
    packet_info = {
        'source_address': decoded_packet_data['source_address'],
        'destination_address': decoded_packet_data['destination_address'],
        'data': decoded_packet_data['data'],
        'control_byte': decoded_packet_data['control_byte']
    }
    
    return packet_info

# add decoder to rf signal intelligence module
rf.add_decoder("X.25 Packet", decode_x25_packet)