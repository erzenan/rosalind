# Conditions and Loops

# Problem
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500

import math
with open("rosalind_ini4.txt", "r") as f:
    a, b = map(int, f.readline().split())
    total = 0
    for i in range(a, b + 1):
        if i % 2 == 1: 
            total += i
    print(total)
    ## toj O(n)
    ## ce hocs O(1) je pa pol
    