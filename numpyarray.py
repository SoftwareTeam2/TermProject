import numpy as np

def pulse(x,position, height, width):
    return height*(x>=position)*(x<=(position+width))
    
x=np.linspace(-5,5,11)
pulse(x,2,1,5)