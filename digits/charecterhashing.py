ch = "aabbccssddeeffghh"
hash_list = [0]*26

for i in ch:
    ascii = ord(i)-97
    hash_list[ascii] += 1

print() 
    