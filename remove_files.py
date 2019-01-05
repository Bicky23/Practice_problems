import os
import glob

# file path
path = 'little pics'

# all contents in directory 'little pics'
for file in os.listdir(path):
    print(file)

print('='*50)

# check if file is JPG
for file in os.listdir(path):
    if file.endswith('.jpg'):
        print(file, "size is", os.path.getsize(os.path.join(path,file)))
        os.remove(os.path.join(path, file))
    
# all contents in directory 'little pics'
for file in os.listdir(path):
    print(file)
