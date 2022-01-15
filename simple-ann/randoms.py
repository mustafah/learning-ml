from matplotlib import pyplot as plt
import numpy as np
from visualize import Visualize
from visualize import VisualizeHelper
class Random:
    def binomial(variations, count):
        return np.random.binomial(n = variations, p = 0.5, size = count)
        
x = Range.generate(start = 1, end = 10)
y = Random.binomial(10, 10)

Visualize.size = 2
Visualize.title = 'Hello'


Visualize.draw(x, y)
Visualize.drawCounts(y)