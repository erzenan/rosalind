import math
with open("rosalind_ini3.txt", "r") as f:
    text = f.readline().strip()
    a, b, c, d = map(int, f.readline().split()) ## readline() includes \n split()
    #                                          ## removes it
    fString = ""
    sString = ""
    # for i in range(len(text)):
    #     if a <= i <= b:
    #         fString += text[i]
    #     if c <= i <= d:
    #         sString += text[i]
    fString = text[a:b+1]
    sString = text[c:d+1]
    print(fString, sString)    





