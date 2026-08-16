# Strings and lists

# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102
# Sample Output

# Humpty Dumpty

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





