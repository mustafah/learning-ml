import numpy as np
from visualize import Visualize
from range import Range

class Activation:
    def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))
    
    def tanh_prime(x):
        return 1 - np.tanh(x)**2
    
    def tanh(x):
        return np.tanh(x)

x = Range.generate(start = -10, end = 10, period = 0.01)

Visualize.size = 2

Visualize.drawFunction(x, Activation.tanh_prime, title = 'tanh_prime')
Visualize.drawFunction(x, Activation.tanh, title = 'tanh')
