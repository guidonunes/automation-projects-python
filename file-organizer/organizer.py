import os
import shutil

path = input("Enter the path of the directory to organize: ")
files = os.listdir(path)

for file in files:
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
