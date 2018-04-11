import sys
import shutil
import os

dest_folder = ["drawable-mdpi", "drawable-hdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]

target_name = sys.argv[1]
dest_name = sys.argv[2]

file_list = []
filenames = os.listdir(".")

for filename in filenames:
    file_split_list = os.path.splitext(filename)
    ext = file_split_list[-1]
    name = file_split_list[0]
    if ext == ".jpg" or ext == ".png":
        if "@" in name and target_name in name:
            multiplier = float(filename.split("@")[1].split("x")[0])
            file_list.append((multiplier, filename))

# sort file list with multiplier, ascending order.
file_list.sort(key=lambda x: x[0])

ext = os.path.splitext(file_list[0][1])[-1]
new_dest_name = dest_name + ext

for i in range(0, len(dest_folder)):
    os.rename(file_list[i][1], new_dest_name)
    print ("rename " + file_list[i][1] + " -> " +  new_dest_name)
    shutil.move(new_dest_name, dest_folder[i])
    print ("move to " + dest_folder[i])
