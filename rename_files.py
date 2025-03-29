#script to renaming all files in a folder 

import os 

#specify the folder where all files are located 
folder_path = "D:/python scripting/automation_projects"

#list all files in the folder 
files = os.listdir(folder_path)

#print the file names 
print("files in the folder: \n")
for file in files:
    print(file)

    