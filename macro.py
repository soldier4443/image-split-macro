import sys
import shutil
import os

def findfiles(resource_type = "drawable"):
    files = []
    dpis = ["-mdpi", "-hdpi", "-xhdpi", "-xxhdpi", "-xxxhdpi"]

    for dpi in dpis:
        for f in os.listdir():
            if f.startswith(resource_type) and f.endswith(dpi):
                files.append(f)
                break
    
    return files

if len(sys.argv) == 3:
    option = "d"
    target_name = sys.argv[1]
    dest_name = sys.argv[2]
elif len(sys.argv) == 4:
    option = sys.argv[1]
    target_name = sys.argv[2]
    dest_name = sys.argv[3]

if option == 'd':
    dest_folder = findfiles()
elif option == 'm':
    dest_folder = findfiles("mipmap")

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

if len(file_list) == 0:
    print ("No match found.")
else:
    # sort file list with multiplier, ascending order.
    file_list.sort(key=lambda x: x[0])

    ext = os.path.splitext(file_list[0][1])[-1]
    new_dest_name = dest_name + ext

    for i in range(0, len(dest_folder)):
        os.rename(file_list[i][1], new_dest_name)
        print ("rename " + file_list[i][1] + " -> " +  new_dest_name)
        shutil.move(new_dest_name, dest_folder[i])
        print ("move to " + dest_folder[i])