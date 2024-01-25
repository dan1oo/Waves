import statistics
import numpy as np
import matplotlib.pyplot as pyplot
from scipy.optimize import curve_fit



def stddev(data):
    n = len(data)
    mean = sum(data)/n
    deviations = [(x-mean)**2 for x in data]
    variance = sum(deviations)/(n-1)
    stddev = np.sqrt(variance)
    return stddev