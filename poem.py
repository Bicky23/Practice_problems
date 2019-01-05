# with open('poem.txt', 'r') as f1, open('output.txt', "w") as f2:
#     for line in f1.readlines():
#         f2.write(line)


with open('output.txt', 'r') as f:
    for line in f.readlines():
        print(line)

import glob
import os

files = os.listdir()
print(glob.glob('*.txt'))