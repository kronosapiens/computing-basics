'''
Python Lab 1

The purpose of this lab is to get you comfortable using functions to
    abstract away useful behavior, as well as how to import outside modules
    to easily acquire new functionality.
'''

'''
Exercise 1: Means

In this exercise, you will write a function which takes
    a list of numbers (floats), and returns the mean,
    or average, of those numbers.
'''

myNumbers = [1.5, 2.5, 2.0]

def myMean(numbers):
    ###################
    ### Your code here!

    mean = sum(numbers) / len(numbers)

    ###################
    return mean

assert (myMean(myNumbers) - 4.0) < .0001, 'Mean wrong or not precise!'

'''
Exercise 2: Means II

In this (short) exercise, you will use an outside module to gain specialized
    functionality, to save you the time of writing it yourself.
'''

from statistics import mean

assert (mean(myNumbers) - 4.0) < .0001


print('Lab 1 complete!')