import struct

#TODO: Determine data rate and framing

class Decoder:
    def __init__(self, data):
        self.data = data

    def baudot_ascii(self):
        output = ''
        for byte in self.data:
            byte = int(byte)
            letter = struct.pack('B', byte).decode('latin-1')
            output += letter
        return output

    def decode(self):
        stream = baudot_ascii(self.data)

        # determine word bit sequence
        # TODO

        words = []
        current_word = ''
        for letter in stream:
            if letter == ' ':
                
                words.append(current_word)
                current_word = ''
            else:
                current_word += letter

        words.append(current_word)

        return words