import os
import shutil
import sys

for f in os.listdir("input"):
  if f.endswith(".png"):
    name = f[:f.find('.')]
    splits = name.split('_')

    color = splits[0]
    shape = splits[1]

    newName = "weight_ic_{}_{}.png".format(shape, color)
    
    print("{} -> {}".format(name, newName))

    os.makedirs("output", exist_ok=True)
    shutil.copy(f, "output/{}".format(newName))