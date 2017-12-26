# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in dirs:
        print("root: ",root)
        print(name)
        #print(os.path.join(root, name))
