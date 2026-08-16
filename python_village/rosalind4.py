# Problem

# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Sample Dataset
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat

# Sample Output
# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat
with open("rosalind_ini5.txt", "r") as f, \
    open("rosalindFile.txt", "w") as nf:
    for line_number, line in enumerate(f, start=1): 
        if line_number % 2 == 0:
            nf.write(line)

        
