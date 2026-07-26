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
    