#script to rename all files with timestamp 

import os
import time 

#scpecify the folder where file is actually located
folder_path="D:/python scripting/automation_projects"

#get all files inside the folder 
files = os.listdir(folder_path)

#loop through each file and rename it 
for file in files:
    old_path = os.path.join(folder_path, file)

    #skip directories
    if os.path.isdir(old_path):
        continue

    #get the extension
    name, ext = os.path.splitext(file)
    #exclude .py files for renaming 
    if ext.lower() == ".py":
        continue
    #generate timestamp
    timestamp = time.strftime("%Y%m%d%H%M%S")
    #new filename with timestamp
    new_name = f"{name}_{timestamp}{ext}"
    new_path=os.path.join(folder_path, new_name)
    #rename file
    os.rename(old_path, new_name)


print("file names renamed successfully: ")

