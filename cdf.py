import numpy as np

def cdf(sample):
    
    x = np.sort(sample)
    y = np.arange(1,len(x) + 1) / len(x)
    return x,y

def draw_cdf(x, y):
    pass
