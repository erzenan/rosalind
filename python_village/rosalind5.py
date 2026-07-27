with open("rosalind_ini6.txt", "r") as f:
    word_counts = {} ## a dictionary stores information as key:value
    for word in f.read().split():
        word_counts[word] = word_counts.get(word, 0) + 1

    for word, counts in word_counts.items(): ##.items() produces pairs as ("word", number)
        print(word, counts) 

## dictionaries rundown
# Dictionaries are used to store data values in key:value pairs.
# dictionary = { "key" : "value", "key2" : "value2"}
# how many items len()
#access items: dictionary.get("key")...> dobis value
# get a list of the keys dictionary.keys()...> seznam keysov values()
# dictionary.items() each item in a dictionary as tuples in a list
## addinf to dictionary tkole dictionary["novValue"] = key