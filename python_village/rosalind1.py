import math
with open("rosalind_ini2.txt", "r") as f:
    a, b = map(int, f.read().split())
csquared= a*a + b*b
print (csquared)
