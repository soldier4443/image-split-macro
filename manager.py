import sys
import shutil
import os

# pre_determined_path = "C:\\Users\\nyh0111\\AndroidStudioProjects\\CodeCalculation\\app\\src\\main\\res"
command = sys.argv[1]

if command == "create" or command == "cd":
    os.mkdir("drawable-mdpi")
    os.mkdir("drawable-hdpi")
    os.mkdir("drawable-xhdpi")
    os.mkdir("drawable-xxhdpi")
    os.mkdir("drawable-xxxhdpi")

if command == "cm":
    os.mkdir("mipmap-mdpi")
    os.mkdir("mipmap-hdpi")
    os.mkdir("mipmap-xhdpi")
    os.mkdir("mipmap-xxhdpi")
    os.mkdir("mipmap-xxxhdpi")

if command == "move":
    for filename in os.listdir("asdf"):
        print(filename)
