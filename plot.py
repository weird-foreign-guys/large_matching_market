import matplotlib.pyplot as plt
#import numpy as np

class Plotter:

    def __init__(self,lower,upper,step):
        #line = list(np.linspace(lower,upper,int((upper-lower)/step)))
        data = {}
        for n in range(lower,upper,step):
            #current value and amount of entries average is based on
            self.data[n] = ("NA",0) 
        self.data = data
    
    def plot(self,n,ratio):
        self.data[n][1] =  
        


