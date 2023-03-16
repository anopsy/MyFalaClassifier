import subprocess
import os
import sys
walk_dir = os.getcwd()
count = 0

for root, subdirs, files in os.walk(walk_dir):
  for file in files:
    if (file.split(".")[-1].lower() == 'ts'):
      filePath = os.path.join(root, file)
      mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
      if os.path.isfile(mp4FilePath):
        continue
      os.system("ffmpeg -i " + "\"" + filePath + "\""  + " \"" + mp4FilePath + "\"")
      count = count + 1
      print ("\"" + filePath + "\"")
print ("Done the total number of file was be converted: ", count)