import bitarray
#import libraries for RF signal analysis
from gnuradio import gr
from gnuradio import blocks
from gnuradio import analog
from gnuradio import filter


#Create blocks for demodulation and decoding of signal
# ********************
#  Demodulation Block
# ********************
#TODO: create demodulation block to extract the baseband signal from RF

class qmacqm9080_demod_block(gr.hier_block2):
    """
    Hierarchical block for demodulating a Q-Mac QM9080 signal
    """

    def __init__(self, rate):
        """
        Create a Q-Mac QM9080 demodulator block
        Args:
            rate: Sample rate of the input signal
        """
        #TODO: create demodulation block
        gr.hier_block2.__init__(self,
            "qmacqm9080_demod_block",
            gr.io_signature(1, 1, gr.sizeof_gr_complex),   # Input signature
            gr.io_signature(1, 1, gr.sizeof_float)) # Output signature

        #Low pass filter
        lpf = filter.fir_filter_ccf(1,firdes.low_pass(1, rate, 5000))
        self.connect(self,lpf)
        
        # FM demodulation
        demod = analog.quadrature_demod_cf(1.0)
        self.connect(lpf,demod)
        
        #Low pass filter
        lpf2 = filter.fir_filter_fcc(1,firdes.low_pass(1, rate, 350))
        self.connect(demod,lpf2)

        #DC removal filter
        dc_remove = filter.dc_blocker_ff(32,False)
        self.connect(lpf2,dc_remove)

        #VOLK scalar
        scaler = blocks.multiply_const_ff(1/32000.0)
        self.connect(dc