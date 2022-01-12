import numpy as np
from helper import Helper

# Simple Neural Network
# Compute XOR of given input
 
class SimpleANN2:
    def __init__(self, input_size = 10):
        np.random.seed(0)
        self.input_size = input_size
        
    def generate_input(self):
        x = np.random.binomial(1, 0.5, self.input_size)
        Helper.count_plot(x)

ann = SimpleANN2()
ann.generate_input()