# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/30/2024
# Description: reverses the order of the elements in a given list

# Defining what will reverse the order of the elements 
def reverse_list(1st):
    start = 0 # Iniitializes start at beginning of list
    end = len(1st) - 1 # Initializes end at end of list
    while start < end: # Continues as long as start value is < end value
        1st[start], 1st[end] = 1st[end], 1st[start] # Swapping start and end
        start += 1 # Moves start forward
        end -= 1 # Moves end backward
