import matplotlib.pyplot as plt
import numpy as np

class VisualizeHelper:
	
    def __init__(self):
        self._size = 1
      
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, s):
        self._size = s
        self.i = 0

        self.fig, self.axes = plt.subplots(s, constrained_layout=True)#, figsize=(5, 5))
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
        self.fig.suptitle(title)
    
    def drawFunction(self, x = None, func = None, start = -10, end = 10, period = 1, title = None):
        if x is None:
            x = np.arange(start, end + period, period)
            
        try:
            y = func(x)
        except:
            y = func()
        
        axes = None
        if self.size > 1:
            axes = self.axes[self.i]
            self.i += 1
        if axes is None:
            axes = plt
        
        if title:
            axes.set_title(title)
            
        axes.grid()
        axes.plot(x,y)
        
        if (self.i >= self.size or self.size == 1):
            plt.show()
            
    def draw(self, x = None, y = None, start = -10, end = 10, period = 1, title = ''):
        if x is None:
            x = np.arange(start, end + period, period)
        
        axes = None
        if self.size > 1:
            axes = self.axes[self.i]
            self.i += 1
        if axes is None:
            axes = plt
        axes.grid(linestyle='-', linewidth=1)
        
        if title:
            axes.set_title(title)
            
        axes.plot(x,y)
        if (self.i >= self.size or self.size == 1):
            plt.show()
            
    def drawCounts(self, y, title = ''):
        import seaborn as sns
            
        axes = None
        if self.size > 1:
            axes = self.axes[self.i]
            self.i += 1
            
        if axes is None:
            axes = plt
            
        if title:
            axes.set_title(title)
            
        # sns.distplot(x, hist=True, kde=True, ax = axes)
        sns.histplot(y, discrete = True, ax = axes)
        # axes.grid()
        
        if (self.i >= self.size or self.size == 1):
            plt.show()
    
        
        
Visualize = VisualizeHelper()