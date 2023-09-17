"""

#TODO: Check if there is a library which will provide the algorithm needed for Harris Citadel I Encryption

def decryptCitadelIEncryption(encrypted_message,key): 
    """
    Decode the Cipher-text using Harris Citadel I Encryption

    Args:
        encrypted_message (str): The cipher-text to be decrypted
        key (int): The key used for encryption

    Returns:
        decrypted_message (str): The original message
    """

    # Initialize the counter to 0
    counter = 0 

    # Initialize the decrypted message
    decrypted_message = ""

    # Iterate through the encrypted message
    for char in encrypted_message:

        # Get the ASCII value of current character 
        ascii_val = ord(char)

        # Perform the XOR operation with the key 
        ascii_val = ascii_val ^ key

        # Increment the counter
        counter += 1

        # If the counter is 3, XOR the character again with 1
        if counter == 3:
            ascii_val = ascii_val ^ 1
            counter = 0
        
        # Append the decrypted character to the message
        decrypted_message += chr(ascii_val)
    
    return decrypted_message


#Function to integrate with your SIGINT framework
def decipher(cipher_text,key):
    """
    Deciphers the given cipher-text using Harris Citadel I Encryption

    Args:
        cipher_text (str): The cipher-text to be decoded.
        key (int): The key used for encryption

    Returns:
        message (str): The decrypted message
    """
    
    # Call the decryptCitadelIEncryption() to decode the cipher-text
    message = decryptCitadelIEncryption(cipher_text,key)

    return message