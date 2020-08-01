# My Python Learnings
# Files and Folders 
# GiridharSalana

#importing Required Libraries
import os
import sys

retVal = os.getcwd()
print("current Working Directory %s" %  retVal)

inp = input("Enter the path of your file: ")
if not inp:
    print("Input is empty")
    os.chdir(r"C:\Users\Admin\Desktop")
    print(r"Directory input Null Going into C:\Users\Admin\Desktop")

else:
    os.chdir(inp)
    print("Directory changed to %s" % inp)