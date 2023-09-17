""" SIGINT Decoder: DZVEI Tonal System

Author: 

Description: This script decodes RF signal intelligence according to the DZVEI Tonal System.

"""

# TODO: Fill in details of how the tonal system works

class TonalCipher:
    
    def __init__(self):
        """ Initializes all variables needed for the cipher. """
        self.tones_to_characters = None
        self.characters_to_tones = None
        
    def encrypt(self, message): 
        """ Encrypts a message according to the DZVEI tonal system. 
        
        Parameters
        ----------
        message: {str}
            The message that is to be encrypted
    
        Returns
        -------
        {str}
            The encrypted message
        """
        encrypted_message = ''
        for character in message:
            encrypted_message += self.characters_to_tones[character]

        return encrypted_message 

    def decrypt(self, encrypted_message): 
        """ Decrypts an encrypted message according to the DZVEI tonal system. 
        
        Parameters
        ----------
        encrypted_message: {str}
            The encrypted message that is to be decrypted
    
        Returns
        -------
        {str}
            The decrypted message
        """
        decrypted_message = ''
        for tone in encrypted_message:
            decrypted_message += self.tones_to_characters[tone]

        return decrypted_message