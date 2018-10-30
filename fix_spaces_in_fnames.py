#https://stackoverflow.com/questions/37912867/renaming-a-single-file-in-python
#https://www.w3resource.com/python-exercises/re/python-re-exercise-23.php
import os

#src = "/home/mthomas/Downloads/baa baa baa.txt"
src = input("Paste filename with path here: ")
dst = src.replace(" ", "_")
if os.path.isfile(src):
    os.rename(src, dst)
    print(dst)