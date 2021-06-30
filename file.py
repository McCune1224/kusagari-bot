import os
import sys
from pathlib import Path

cwd = os.getcwd()

print(os.path.isdir(cwd))

cwd = os.path.join(cwd, "droidSounds")
print(cwd)

content = os.listdir(cwd)

if sys.argv[1] + ".mp3" in content:
    print("yes")
else:
    print("no")

droid = os.listdir(os.path.join(os.getcwd(), "droidSounds"))

d2 = os.path.join(cwd, "droidSounds", "roger.mp3")
print(d2)


