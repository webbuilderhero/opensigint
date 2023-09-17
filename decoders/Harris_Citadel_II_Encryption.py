#TODO: Research Harris Anthem Encryption Protocol to help build this decoder

# Harris Citadel II Decryptor
import base64, binascii

'''
This script is built to decode Harris Citadel II encrypted transmissions
This script is a part of the RF Signal Intelligence framework

Author: [Pseudonym]
'''

#sender/receiver will enter the keys for the crytogram
sender_key = input('Enter sender key: ')
receiver_key = input('Enter receiver key: ')

#get the encrypted message
encrypted_message = input('Enter encrypted message:  ')

#decode the encrypted message
ascii_message = base64.b64decode(encrypted_message).decode('utf-8')

#perform the deobfuscation using the sender/receiver keys
key1 = int(sender_key, 16)
key2 = int(receiver_key, 16)
decrypted_message = ""

#decrypt the message using XOR
for i in range(len(ascii_message)):
 decrypted_message += chr( ord(ascii_message[i])^key1^key2)

#print the decoded message
print('Decrypted message: ', decrypted_message)