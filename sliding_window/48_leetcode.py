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