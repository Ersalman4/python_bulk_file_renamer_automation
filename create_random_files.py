#script to generate some random files to test my project 

import os

#folder where test files are going to created 
folder_path = "D:/python scripting/automation_projects"

#ensure that folder is actually existed 
os.makedirs(folder_path, exist_ok=True)

#create 10 dummy files in the folder 

for i in range(1, 11):
    file_name = f"test_file_{i}.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w")as f:
        f.write(f"This is test file {i}\n")
    
print("Test files created successfully")


