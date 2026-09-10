# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" # you can use three double-quotes to write multi-line comments
XXX Write your pseudocode here XXX
"""
N=int(input("Number of Fibonacci numbers to sum: ")) # user input an intputs value for N, which represents the first N numbers in the Fibonacci sequence to sum
a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # initialize a counter to keep track of how many Fibonacci numbers have been added to the total sum
total=0 # initialize a variable to keep track of the total sum of the Fibonacci numbers

while count < N: # loop until we have sum of first N Fibonacci numbers
    total += a # add the current Fibonacci number to the total sum
    a, b = b, a + b # update a and b to the next two Fibonacci numbers in the sequence
    count+= 1 # increment the counter by 1
print(total) # print the total sum of the first N Fibonacci numbers

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # set N to 6 to retrieve the the sum of the first 6 numbers in the Fibonacci sequence

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # initialize a counter to keep track of how many Fibonacci numbers have been added to the total sum
total = 0 # initialize a variable to keep track of the total sum of the Fibonacci numbers

while count < N: # loop until we have the sum of the first N numbers in the Fibonacci sequence
    total = total + b # add the current Fibonacci number to the total sum

    next_value = a + b # obtain next Fibonacci number in the sequence
    a = b # update a to the previous Fibonacci number
    b = next_value # update b to the next Fibonacci number in the sequence

    count+= 1 # increment the counter by 1

print(total) # print total sum of the first N numbers in the Fibonacci sequence

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

import numpy as np  # import the numpy library to use its functions for numerical calculations
fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # create a list of the first 10 numbers in the Fibonacci sequence
std_dev = np.std(fibonacci_numbers) # calculate the standard deviation of the Fibonacci numbers using numpy's std function
print("The standard deviation of the first 10 Fibonacci numbers is:", std_dev) # print the calculated standard deviation

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

N = [5, 10, 15, 20, 25, 30] # create a list of values for N to calculate the sum of the first N numbers in the Fibonacci sequence
def sum_fibonacci(n): # define a function that takes an integer n as input
    a, b = 0, 1 # initialize the first two Fibonacci numbers
    total = 0 # initialize a variable to keep track of the total sum of the Fibonacci numbers
    for _ in range(n): # loop n times to calculate the sum of the first n Fibonacci numbers
        total += a # add the current Fibonacci number to the total sum
        a, b = b, a + b # update a and b to the next two Fibonacci numbers in the sequence
    return total # return the total sum of the first n Fibonacci numbers
sums = [sum_fibonacci(n) for n in N] # calculate the sums for each value of N
print("The sums of the first N Fibonacci numbers are:", sums) # print the list of sums

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0 #intitalized as an integer value 0 to avoid TypeError when comparing with limit
    b = 1 #intitalized as an integer value 1 to allow for correct Fibonacci sequence generation
    index = 0 # initialize the index variable to 0 before the while loop to avoid UnboundLocalError

    while a <= limit: # this line contains a TypeError because 'a' is a string and 'limit' is an integer; to fix this error, the variable 'a' needs to be initialized as the integer value 0 (rather than the string "0") before the while loop
        next_value = a + b # integers a and b to get the next Fibonacci number in the sequence
        a = b
        b = next_value
        index += 1 # this line contains a UnboundLocalError because 'index' is not defined before it is used; to fix the error, the variable 'index' needs to be initialized to 0 before the while loop

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)
# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_even_fib(limit):
    a, b = 0, 1 # initialize the first two Fibonacci numbers
    total = 0 # initialize a variable to keep track of the total sum of the odd Fibonacci numbers
    while b <= limit: # loop until the current Fibonacci number is greater than the limit
        if b % 2 != 0:  # this line checks if the Fibonacci number is odd and adds it to the total sum if it is
            total += b # add the current Fibonacci number to the total sum if it is odd
        a, b = b, a + b # update a and b to the next two Fibonacci numbers in the sequence
    return total


# Add your test cases here

print("Sum of odd Fibonacci numbers up to 1:", sum_even_fib(1))    # Expected: 1
print("Sum of odd Fibonacci numbers up to 10:", sum_even_fib(10))   # Expected: 10
print("Sum of odd Fibonacci numbers up to 20:", sum_even_fib(20))   # Expected: 23
print("Sum of odd Fibonacci numbers up to 50:", sum_even_fib(50))   # Expected: 44
print("Sum of odd Fibonacci numbers up to 100:", sum_even_fib(100))  # Expected: 188
print("Sum of odd Fibonacci numbers up to 300:", sum_even_fib(300))  # Expected: 421


# %%
