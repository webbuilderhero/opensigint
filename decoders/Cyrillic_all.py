#!/usr/bin/env python

#TODO: figure out how to do extendable language support (in this case Cyrillic) 

import binascii

def cyrillic_decoder(cyrillic_bytes):
    cyrillicString = binascii.unhexlify(cyrillic_bytes).decode('cp1251')
    return cyrillicString
    
def main(cyrillic_bytes):
    cyrillic_string = cyrillic_decoder(cyrillic_bytes)
    return cyrillic_string

if __name__ == '__main__':
    main()