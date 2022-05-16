import math

# Write a function in Python that accepts one numeric parameter.
# This parameter will be the measure of an angle in radians.
# The function should convert the radians into degrees and then return that value.
# Do not use external libraries for this exercise.

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    print(degrees)
    return degrees

radians_to_degrees(7)
