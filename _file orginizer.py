# import os

# folder = "./Linked_list"
# os.makedirs(folder, exist_ok=True)

# for i in range(2, 51):
#     filename = os.path.join(folder, f"({i})_.py")
#     with open(filename, "w") as f:
#         pass



import os
import re


def rename_files_sequentially(folder_path, start_number=7, keep_up_to=6, dry_run=True):
    """
    Renumber .py files so the number in (N)_ is sequential.

    - Files already numbered (1)_ .. (keep_up_to)_ are kept as-is.
    - Every other .py file is renumbered starting at `start_number`, in order.
    - Only the (N)_ part changes; the rest of the filename stays the same.

    Set dry_run=False to actually rename.
    """
    numbered = re.compile(r'^\((\d+)\)_?')

    to_rename = []
    for filename in os.listdir(folder_path):
        full = os.path.join(folder_path, filename)
        if os.path.isdir(full):
            continue
        if not filename.endswith('.py'):
            continue

        m = numbered.match(filename)
        if m and int(m.group(1)) <= keep_up_to:
            print(f"  [KEEP] {filename}")
            continue

        to_rename.append(filename)

    # Sort by the EXISTING number (numeric, not text) so order is preserved.
    # Files with no number go last, sorted by name.
    def sort_key(name):
        m = numbered.match(name)
        return (0, int(m.group(1))) if m else (1, name.lower())

    to_rename.sort(key=sort_key)

    print(f"\n{'='*60}\nFILES TO BE RENAMED ({len(to_rename)}):\n{'='*60}")

    counter = start_number
    plan = []
    for filename in to_rename:
        rest = re.sub(r'^\(\d+\)_?', '', filename).strip('_')
        new_name = f"({counter})_{rest}"
        plan.append((filename, new_name))
        print(f"  {filename}\n    -> {new_name}\n")
        counter += 1

    print('='*60)

    if dry_run:
        print("DRY RUN - nothing changed. Set dry_run=False to rename.")
        return

    for old_name, new_name in plan:
        os.rename(os.path.join(folder_path, old_name),
                  os.path.join(folder_path, new_name))
        print(f"  Renamed: {old_name} -> {new_name}")
    print(f"\nDone. Renamed {len(plan)} files.")


FOLDER_PATH = r"C:\Users\Mateti sai pranay\Downloads\analytics_open_data\DSA_python\Arrays"

# Step 1: preview (safe — changes nothing)
# rename_files_sequentially(FOLDER_PATH, start_number=7, keep_up_to=6, dry_run=True)

# Step 2: when the preview looks right, set dry_run=False below and run again
rename_files_sequentially(FOLDER_PATH, start_number=7, keep_up_to=6, dry_run=False)
