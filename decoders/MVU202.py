import codecs

# decoder for MVU-202

def decodeMVU202(binary_string): 
    decoded_string = ""
    #TODO: Implement MVU-202 Binary Decoding Algorithm

    #Initialize dictionary of binary strings and their corresponding characters
    binary_characters = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3', 
        '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
        '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', 
        '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f', 
    }

    #Split binary string into groups of 4
    binary_groups = [binary_string[4*i : 4*i+4] for i in range(len(binary_string) / 4)]

    #Convert binary_groups into decoded string
    for binary_group in binary_groups:
        decoded_string += binary_characters[binary_group]
    
    return decoded_string

#Decode a given binary string
def name_decoder(binary_string):
    #Retrieve the code, function, and length of data from binary_string
    code_string = binary_string[:4]
    func_string = binary_string[4:8]
    length = binary_string[8:10]
    #Decode the rest of the data based on function specified
    data = binary_string[10:]
    #MVU-202 decoding
    if func_string == '0011': 
        return [code_string, func_string, length,  decodeMVU202(data)]
    else:
        return [code_string, func_string, length, data]