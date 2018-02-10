import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt

# Net Parameter
BATCH_START = 0
TIME_STEPS  = 20
BATCH_SIZE  = 50
INPUT_SIZE  = 1
OUPUT_SIZE  = 1
CELL_SIZE   = 10
LR          = 0.006
def get_batch():
    global BATCH_START, TIME_STEPS
    xs = np.arange() / (10 * np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEPS
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]

class LSTMRNN(obejct):
    def __init__(self, n_steps, input_size, output_size, cell_size, batch_size):
        self.n_steps     = n_steps
        self.input_size  = input_size
        self.output_size = output_size

    def add_input_layer(self, ):
        return

    def add_cell(self):
        return 
    
    def add_output_layer(self):
        return

    def compute_cost(self):
        return

    @staticmethod
    def ms_errror(labels, logits):
        return

    def _weight_variable(self, shape, name='weights'):
        return

    def _bias_variable(self, shape, name='biases'):
        return


if __name__ == '__main__':
