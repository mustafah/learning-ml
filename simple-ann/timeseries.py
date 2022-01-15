import numpy as np
from visualize import Visualize
from range import Range
num_epochs = 100
total_series_length = 500
truncated_backprop_length = 15
state_size = 4
num_classes = 2
echo_step = 3
batch_size = 5
num_batches = total_series_length//batch_size//truncated_backprop_length

Visualize.size = 1
x = Range.generate(1, total_series_length)
y = np.random.choice(2, total_series_length, p=[0.5, 0.5])
print(y, len(y))

Visualize.draw(x, y)