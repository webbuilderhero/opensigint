# TODO: Get details on D91B ALE to plug into decoder
# 
# Decoder for XD-D91B ALE

import csv 

# Define list objects for coding and mapping each ALR
ALR_CODING = []
ALE_MAPPING = []

# Read the CSV containing the ALE codes
with open('ale_mapping.csv', 'r') as csvfile:
    
    # Create CSV reader object
    reader = csv.reader(csvfile)
    
    # Iterate through each row in the CSV 
    for row in reader:
        
        # Append the individual codes to the ALR_CODING list 
        ALR_CODING.append(row[0])
        
        # Create a dictionary mapping for ALR codes
        ALE_MAPPING.append({
            "code": row[0],
            "description": row[1]
        })

# Define function to decode ALE codes
def decode_ale(input):

    # Iterate through the ALE coding list
    for code in ALR_CODING:
        # Check if given input is found in coding list
        if input == code:
            # Construct output string
            output = "XD-D91B ALE:\nCode: {0}\nDescription: {1}".format(code, ALE_MAPPING[ALR_CODING.index(code)]["description"])
            # Return output string
            return output