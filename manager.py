import sys
import shutil
import os

# pre_determined_path = "C:\\Users\\nyh0111\\AndroidStudioProjects\\CodeCalculation\\app\\src\\main\\res"
command = sys.argv[1]

if command == "create":
    os.mkdir("drawable-xhdpi")
    os.mkdir("drawable-xxhdpi")
    os.mkdir("drawable-xxxhdpi")

if command == "move":
    for filename in os.listdir("asdf"):
        print(filename)
