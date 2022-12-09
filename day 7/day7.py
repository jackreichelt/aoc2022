#!/usr/bin/env python3

TOTAL_SIZE = 70000000
NEEDED_FREE = 30000000

data = [x.strip() for x in open("data.txt").readlines()]

class Folder:
  def __init__(self, name, parent=None):
    self.name = name
    self.parent = parent
    self.subfolders = {}
    self.files = {}
    
  def addSubFolder(self, subName):
    newSub = Folder(subName, parent=self)
    self.subfolders[subName] = newSub
    return newSub
  
  def addFile(self, fName, fSize):
    self.files[fName] = fSize
    
  def folderSize(self):
    fileSizes = sum(self.files.values())
    folderSizes = sum([f.folderSize() for f in self.subfolders.values()])
    return fileSizes + folderSizes
  
  def isSmall(self):
    return self.folderSize() <= 100000
  
root = Folder("/")
workingDir = root

allFolders = [root]

for line in data[1:]: # skip initial cd
  if line.startswith("$"):
    # is a command
    if line.startswith("$ cd "):
      destination = line.split(" ")[2]
      if destination == "..":
        workingDir = workingDir.parent
      else:
        workingDir = workingDir.subfolders[destination]
    elif line.startswith("$ ls "):
      pass # do nothing here
  else:
    # is a file
    if line.startswith("dir"):
      newFolder = workingDir.addSubFolder(line.split(" ")[1])
      allFolders.append(newFolder)
    else:
      fSize, fName = line.split(" ")
      workingDir.addFile(fName, int(fSize))
    
print("All small folders:", sum([x.folderSize() for x in allFolders if x.isSmall()]))
print()

foldersBySize = sorted(allFolders, key=lambda x : x.folderSize())

freeSpace = TOTAL_SIZE - root.folderSize()
neededClearance = NEEDED_FREE - freeSpace

for f in foldersBySize:
  if f.folderSize() >= neededClearance:
    print("Folder to delete and size:", f.name, f.folderSize())
    break