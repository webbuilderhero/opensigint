# TODO: Do research on voice inversion encryption

# Create a Decoder for Voice Inversion

# import necessary libraries 
import numpy as np
import matplotlib.pyplot as plt

# Input frequency range 
MIN_FREQ = 200 
MAX_FREQ = 3500 

# Output frequency range 
DECRYPTED_MIN_FREQ = 1000 
DECRYPTED_MAX_FREQ = 2000 

def decrypt_message(encrypted_message, min_freq, max_freq, decrypted_min_freq, decrypted_max_freq):
    
  # Get length and initialize decrypted array 
  N = encrypted_message.size 
  decrypted_messsage = np.zeros(N) 

  # Apply the decoding algorithm 
  for i in range(N): 
    decrypted_messsage[i] = decrypted_min_freq + \
        (encrypted_message[i] - min_freq) * \
        (decrypted_max_freq - decrypted_min_freq) / \
        (max_freq - min_freq)

  return decrypted_messsage

# Test the decryption 
if __name__ == "__main__": 
  encrypted_message = np.array([3400, 1250, 521, 4213, 1800, 2501, 3251])

  # display original message 
  plt.plot(encrypted_message) 
  plt.title("Original Encrypted Message") 
  plt.show(block=False) 

  # Decrypt message 
  decrypted_message = decrypt_message(encrypted_message, 
                                      MIN_FREQ, MAX_FREQ, 
                                      DECRYPTED_MIN_FREQ, 
                                      DECRYPTED_MAX_FREQ) 

  # display decrypted message 
  plt.plot(decrypted_message) 
  plt.title("Decrypted Message") 
  plt.show()