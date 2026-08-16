# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT
with open("bioinformatics_stronghold/rosalind_revc.txt", "r") as f:
    text = f.readline().strip()
    out = ""
    textlen = len(text)
    for i, nd in enumerate(text):
        if nd == "A":
            out = "T" + out
        elif nd == "T":
            out = "A" + out
        elif nd == "C":
            out = "G" + out
        elif nd == "G":
            out = "C" + out
    print(out)
        
### how to reverse a string using python slicing [start : stop : step]
# positive step → omitted start means beginning
# negative step → omitted start means end
#  [::-1]

# GOOD solution would be 
# out = text.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
# out = out.upper()[::-1]
