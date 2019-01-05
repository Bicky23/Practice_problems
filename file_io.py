import os
import glob

# path
path = 'images'

# display full path of all files and folders
print(os.listdir(path))
print('='*20)

# full path of images directory
# full_path = os.path.join(path, "*.png")

# display all PNG files
#for file in glob.glob(full_path):
   # print(file)
#print('='*20)

# rename all png files to jpg files
for current_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        old_name = os.path.join(current_folder, file_name)
        new_name = old_name[:-4] + ".jpg"
        os.rename(old_name, new_name)

# display all contents of images
for file in os.listdir(path):
    print(file)
print('='*20)

# check if files were renamed
for file in os.listdir(path):
    fp = os.path.join(path, file)
    if os.path.isdir(fp):
        print("It is a folder!")
    else:
        if fp.endswith('.jpg'):
            print("Successfully renamed")
        else:
            print("Failed!")
