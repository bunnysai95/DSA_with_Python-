import os

folder = "./Linked_list"
os.makedirs(folder, exist_ok=True)

for i in range(2, 51):
    filename = os.path.join(folder, f"({i})_.py")
    with open(filename, "w") as f:
        pass



