# TODO: Research signal information belongs to which group

import os

# decode JFRC-F70 ALE
def decode(message):
    cw = 21 #Character Wheel
    bld = [] #Blank List Data
    d_message = "" #Decoded Message
    for i in range(len(message)):
        c = message[i]
        #Rotate the character wheels
        cw = (cw + 1)%27
        if c in ('-','.'):
            bld.append(c)
        else:
            bld.append(chr(ord(c) + cw))

    return d_message.join(bld)

#Main Program
x = input("Enter coded message: ")
decoded_m = decode(x)
print("Decoded Message: ", decoded_m)

#Run the script
if __name__ == "__main__": 
    os.system("python main.py")