#TODO: Process JFRC-F70 Data

import numpy as np

def decode_JFRCF70Data(data, fs):
    
    # Create data solutions
    data_solutions = []
    
    # Calculate number of samples
    N = len(data)
    
    # Calculate sample time
    T = 1/fs
    
    # Perform Fourier Transform
    Xk = np.fft.fft(data)
    
    # Calculate Frequencies 
    f = np.linspace(0.0, 1.0/(2.0*T), N//2)
    
    # Calculate magnitude of the signal
    Xk_abs = np.abs(Xk[0:N//2])
    
    # Detect peak frequency
    k = np.argmax(Xk_abs)
    
    # Calculate peak frequency
    f_peak = f[k]
    
    # Functions to determine the wave type
    if f_peak < 2000:
        waveType = 'DC current'
    elif 2000 <= f_peak < 10000:
        waveType = 'AC current'
    elif 10000 <= f_peak < 20000:
        waveType = 'Resistance'
    elif 20000 <= f_peak < 30000:
        waveType = 'Capacitance'
    else:
        waveType = 'Inductance'
        
    # Append solutions to list
    data_solutions.append({
        'frequency': f_peak,
        'waveType': waveType
    })

    # Return results
    return data_solutions