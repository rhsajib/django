nums = [4,1,-1,2,-1,2,3]
k = 2



nums_dict = {i:nums.count(i) for i in set(nums)}
print(nums_dict)
sorted_dict = sorted(nums_dict.keys(), key=lambda x: nums_dict[x], reverse=True)
print(sorted_dict)
print(sorted_dict[:k])