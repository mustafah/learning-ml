import numpy as np


class Range:
    def generate(start = 1, end = 10, period = 1):
        return np.arange(start, end + period, period)