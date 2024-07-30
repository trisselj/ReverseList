# Author: Jake Trissel
# Github Username: trisselj
# Date: 07/30/2024
# Description: reverses the order of the elements in a given list

# Defining what will reverse the order of the elements 
def reverse_list(first):
    start = 0 # Iniitializes start at beginning of list
    end = len(first) - 1 # Initializes end at end of list
    while start < end: # Continues as long as start value is < end value
        first[start], first[end] = first[end], first[start] # Swapping start and end
        start += 1 # Moves start forward
        end -= 1 # Moves end backward
