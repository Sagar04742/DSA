n = [1,2,3,6,5,2,3,1,4,8,9,8,9,5,6,5,6,5,6,2,3,1,2,4,5,8,5,8,5,6,5,1]
m = [1,5,4,9,8,6,2,51,6]

# hash_list = [0]*11

# for i in n:
#     hash_list[i] +=1

# for i in m:
#     if i<0 or i>10:
#         print(f"{i} is not present in the list")
#     else:
#         print(f"{i} is present {hash_list[i]} times")


hash_dict = dict()


for i in n:
    hash_dict[i] = hash_dict.get(i, 0) + 1

for i in m:
    if i in hash_dict:
        print(f"{i} is present {hash_dict[i]} times")
    else:
        print(f"{i} is not present in the list")

