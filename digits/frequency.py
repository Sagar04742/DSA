# x = [1,2,3,4,512,3,54,6,52,3,0,12,1,2]

# freq_map = dict()

# for i in range(len(x)):
#     if x[i] in freq_map:
#         freq_map[x[i]] += 1
#     else:
#         freq_map[x[i]] = 1
        
# print(freq_map)

#-------------------------------------------

x = [1,2,3,4,512,3,54,6,52,3,0,12,1,2]

freq_map = dict()

for i in range(len(x)):
    freq_map[x[i]] = freq_map.get(x[i],0) + 1

print(freq_map)
    