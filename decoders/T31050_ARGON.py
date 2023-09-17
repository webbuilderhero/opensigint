# TODO: Reconfigure the decoder to fit into the framework for signal intelligence.

# Decodes the signal: T-310/50 ARGON
def decodeT310_50Argon(signal):
  # Get the transmission type
  transmission_type = signal.split("/")[0]
  
  # Get the power
  power = signal.split("/")[1]
  
  # Get the type of gas
  gas_type = signal.split("/")[2]
  
  # Construct a decoded object 
  decoded = {
      "transmission_type": transmission_type,
      "power": power,
      "gas_type": gas_type
      }
  
  return decoded