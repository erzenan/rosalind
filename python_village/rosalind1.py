# Variables and Some Arithmeticclick to expand
# Problem
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
# Sample Dataset
# 3 5
# Sample Output
# 34
import math
with open("rosalind_ini2.txt", "r") as f:
    a, b = map(int, f.read().split())
csquared= a*a + b*b
print (csquared)
