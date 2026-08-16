# The Second Nucleic Acid
# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.
# Sample Dataset
# GATGGAACTTGACTACGTAAATT
# Sample Output
# GAUGGAACUUGACUACGUAAAUU
with open("bioinformatics_stronghold/rosalind_rna.txt", "r") as f:
    rna = ""
    text = f.readline().strip()
    for i in text:
        if i == "T":
            rna += "U"
        else:
            rna += i
    print(rna)
## much much shorter version
# text = "GATGGAACTTGACTACGTAAATT"
# print(text.replace("T", "U"))