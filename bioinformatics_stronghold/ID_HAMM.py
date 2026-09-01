# Counting Point Mutations
# Problem
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7
with open("bioinformatics_stronghold/rosalind_hamm.txt", "r") as f:
    s1 = f.readline().strip() 
    s2 = f.readline().strip()
    Hammingdist = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            Hammingdist += 1

    print(Hammingdist)

