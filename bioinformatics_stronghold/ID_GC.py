# # Computing GC content

# Problem
# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.
# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.
# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Sample Dataset
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
# TCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
# ATATCCATTTGTCAGCAGACACGC
# >Rosalind_0808
# CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
# TGGGAACCTGCGGGCAGTAGGTGGAAT

# Sample Output
# Rosalind_0808
# 60.919540
with open("bioinformatics_stronghold/rosalind_gc.txt", "r") as f:
    maxFname = ""
    maxProcentage = 0
    Fname = f.readline().strip()
    while Fname != "" :
        # print(f" ime filea je {Fname}")
        FDNA = f.readline().strip()
        CGValue = 0
        CGProcentage = 0 
        chain = 0
        while(FDNA != "" and FDNA[0] != '>'):
            # print(FDNA)
            CGValue += FDNA.count("C")
            CGValue += FDNA.count("G")
            chain += len(FDNA)
            FDNA = f.readline().strip()
            # print(f"FDNA JE TOOLEEE {FDNA}")
        CGProcentage = CGValue / chain
        # print(f"CGProc{CGProcentage}")
        if  CGProcentage > maxProcentage:
            maxProcentage = CGProcentage
            maxFname = Fname
        if FDNA == "":
            break
        else:
            Fname = FDNA
    print(maxFname[1:])
    print(f"{maxProcentage * 100:.3f}")

    
