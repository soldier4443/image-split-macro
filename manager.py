import sys
import shutil
import os

# pre_determined_path = "C:\\Users\\nyh0111\\AndroidStudioProjects\\CodeCalculation\\app\\src\\main\\res"
command = sys.argv[1]

if len(sys.argv) > 2:
    prefix = sys.argv[2]
else:
    prefix = ""

if command == "create" or command == "cd":
    os.mkdir("drawable-{}mdpi".format(prefix))
    os.mkdir("drawable-{}hdpi".format(prefix))
    os.mkdir("drawable-{}xhdpi".format(prefix))
    os.mkdir("drawable-{}xxhdpi".format(prefix))
    os.mkdir("drawable-{}xxxhdpi".format(prefix))

if command == "cm":
    os.mkdir("mipmap-{}mdpi".format(prefix))
    os.mkdir("mipmap-{}hdpi".format(prefix))
    os.mkdir("mipmap-{}xhdpi".format(prefix))
    os.mkdir("mipmap-{}xxhdpi".format(prefix))
    os.mkdir("mipmap-{}xxxhdpi".format(prefix))

if command == "move":
    for filename in os.listdir("asdf"):
        print(filename)
