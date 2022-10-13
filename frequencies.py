"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for x in items:
        if x in frequencies:
            frequencies[x] += 1
        else:
            frequencies[x] = 1
    return frequencies
