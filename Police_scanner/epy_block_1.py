import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    def __init__(self, sample_rate=1.0):  # only default arguments here
        gr.sync_block.__init__(
            self,
            name='FFT Shift',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.sample_rate = sample_rate

    def work(self, input_items, output_items):
	print (input_items[0][:])
        if (input_items[0][:] < 0.0):
	    print ("if")
            output_items[0][:]= input_items[0][:] - self.sample_rate
        else:
   	    print ("else")
            output_items[0][:]= input_items[0][:]
	result =  float(output_items[0][:])  	
	print result     
	return result
