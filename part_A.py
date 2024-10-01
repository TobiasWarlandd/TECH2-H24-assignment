"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
import numpy
from math import sqrt

num_lst = [1, 2, 3, 4, 5]

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    # Computes the mean of x 
    sumx = 0 
    c1 = 0
    for i in x:
        c1 += 1
        sumx = sumx + i 
    
    mean = sumx/c1
   
    # Computes the mean of squares 
    sumS = 0 
    c2 = 0
    for i in x:
        c2 += 1
        sumS = sumS + i ** 2
    
    meanS = sumS/c2
    print(meanS)
    #Comptues the variance 
    variance = meanS - mean**2
    
    # Compute the standard deviation 
    standard_deviation = float(sqrt(variance))

    return standard_deviation 

print(std_loops(num_lst))

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    
    meanx = sum(x)/len(x)
    

    meanS = sum(i**2 for i in x)/len(x)
   

    variance = meanS - meanx**2
   
    standard_deviation = float(sqrt(variance))

    return standard_deviation

print(std_builtin(num_lst))


#Using the std function from numpy
print(numpy.std(num_lst))