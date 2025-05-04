import os
import random
import string

# Folder to work in
folder = "./dailyDocs"
os.makedirs(folder, exist_ok=True)

# 🔥 Clear the folder first
for file in os.listdir(folder):
    file_path = os.path.join(folder, file)
    if os.path.isfile(file_path):
        os.remove(file_path)


# 🔁 Create random files that start with "demo"
def random_filename(length=8):
    random_part = "".join(
        random.choices(string.ascii_letters + string.digits, k=length)
    )
    return f"demo{random_part}.txt"


for _ in range(20):
    filename = random_filename()
    filepath = os.path.join(folder, filename)

    with open(filepath, "w") as f:
        f.write(f"This is {filename}")

    print(f"✅ Created {filepath}")
