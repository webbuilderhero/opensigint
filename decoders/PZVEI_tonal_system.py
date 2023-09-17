#include <stdio.h>
#include <stdlib.h>

// TODO: Figure out how to decode PZVEI tonal system

int main(int argc, char *argv[]) {
    /* Read signal data */
    short *sample_ data;  // array of sample data
    int num_samples;      // number of samples in array
    int i;

// Initialize array
    sample_data = (short *) malloc (num_samples * sizeof (short));

// TODO: Read signal data into array

// TODO: Decode PZVEI tonal system 

    decodePZVEI(sample_data, num_samples);

    // Free memory
    free (sample_data);
    
    return 0;
}

/**
* Decodes the PZVEI tonal data
*
* @param sample_data The sample data array
* @param num_samples The number of samples
*
* @return 0 if successful, non-zero otherwise
*/
int decodePZVEI(short *sample_data, int num_samples) {
// TODO: Implement the PZVEI decoding algorithm
    return 0;
}