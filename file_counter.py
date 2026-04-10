import os

count = sum(1 for f in os.listdir('./Arrays_Strings') if f.endswith('.py'))
print(count)


