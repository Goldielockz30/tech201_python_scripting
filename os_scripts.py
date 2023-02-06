import os

# 1. Create a directory

# Directory
directory = "test_dir"

# Parent Directory
parent_dir = "C:/Users/ahimb"

# Path
path = os.path.join(parent_dir, directory)

# Create the DIR
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# 2. Make a file in the new directory

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Write to the new file
# use the open function, within the open function this is the file I want to open and I want to write to it
with open(os.path.join(path, filename), "w") as file1:
    toFile = "Contents of my new file"
    file1.write(toFile)
print("File" + filename + " created in " + directory + " folder")