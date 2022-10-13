"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        if(type(x)is not str):
            x = str(x)
        if x in frequencies:
            frequencies[x] += 1
        else:
            frequencies[x] = 1
    return frequencies
