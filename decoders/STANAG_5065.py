#TODO: Research decoder compatibility with framework

#Imports
import datetime 
import matplotlib.pyplot as plt 
import numpy as np 

#Variables 
stanag_5065_array = [] #Array for values from STANAG 5065 

#Functions
def load_data():
    '''Function to load STANAG 5065 data'''
    fp = open('STANAG-5065.dat', 'r')  #Open STANAG 5065 file 
    for line in fp.readlines():  #Read each line in file 
        if len(line.strip()) > 0: #If line is not null 
            stanag_5065_array.append(float(line)) #Append value to stanag_5065_array
    fp.close() #Close file 

def decode_data():
    '''Function to decode data from STANAG 5065'''
    #Perform necessary computations to decode data 

    #Plot data 
    t = np.arange(len(stanag_5065_array)) 
    plt.plot(t,stanag_5065_array) 
    plt.xlabel('Time (s)') 
    plt.ylabel('Amplitude (V)') 
    plt.title('STANAG 5065 Decoded Signal') 
    plt.grid(True, which='both') 
    plt.axhline(y=0, color='k') 
    plt.show()

#Main Function
def main():
    #Load data 
    load_data()
    #Decode data 
    decode_data()

if __name__ == "__main__": 
    main()