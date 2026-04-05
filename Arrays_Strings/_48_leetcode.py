# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict
maps = defaultdict(list)
result = []
for s in strs:
    sorted_s=tuple(sorted(s))
    maps[sorted_s].append(s)
for values in maps.values():
    result.append(values)
    
print(result)