s = "anagram"
t = "nagaram"

for i in s:
    if i not in t:
        print("False")
        break
else:
    print("True")

# optimzed solution
print(sorted(s) == sorted(t))