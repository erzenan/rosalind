with open("rosalind_ini5.txt", "r") as f, \
    open("rosalindFile.txt", "w") as nf:
    for line_number, line in enumerate(f, start=1): 
        if line_number % 2 == 0:
            nf.write(line)

        
