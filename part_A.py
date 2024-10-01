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
   
    sumx = 0 
    counter = 0
    sumS = 0 
    for i in x:
        counter += 1                                  
        sumx = sumx + i                             # Computes the sum of X 
        sumS = sumS + i ** 2                        # Computes the sum of Squares S 

    mean = sumx/counter                             # The mean of X 
    meanS = sumS/counter                            # The mean of Squares S

    #Comptues the variance 
    variance = meanS - mean**2
    
    # Compute the standard deviation 
    standard_deviation = float(sqrt(variance))

    return standard_deviation 



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


def main():
    print(f'The standard deviation when using soley loops is {std_loops(num_lst)}')
    print(f'The standard deviation when using built in functions is {std_builtin(num_lst)}')
    print(f'The standard deviation when using the numpy function std() {numpy.std(num_lst)}')


if __name__ == "__main__":
    main()