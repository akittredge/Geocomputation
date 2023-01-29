# Andrew Kittredge
# GTECH 731
# Assignment 1

# Task 1: Get the Python version on your computer
import platform
print(platform.python_version())

# Task 2: Write Python code to do the following:
#     - Generate a list of random numbers using random module in Python
#     - Calculate the mean value for the list by looping through its elements
#     - Calculate the variance of the list

# Generate a list of random numbers using random
from random import seed, sample
seed(731)
numberList_1 = sample(range(0, 25, 1), 10)
print(numberList_1)

# Calculate the mean of the list by looping through its elements
def listMean(numberList):
    sum = 0
    for i in numberList:
        sum = sum + i
    mean = sum / len(numberList)
    print(mean)
listMean(numberList_1)

# Calculate the variance of the list
def listVar(numberList):
    sum = 0
    for i in numberList:
        sum = sum + i
    mean = sum / len(numberList)
    sum_of_squares = 0
    for i in numberList:
        sum_of_squares = sum_of_squares + ((i - mean)**2)
    var = sum_of_squares / len(numberList)
    print(var)
listVar(numberList_1)

