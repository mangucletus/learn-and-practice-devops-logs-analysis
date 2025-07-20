# 1. What are some key features of python that make it ideal for devops automation
# - Ease of use, cross-platform support - comprehensive libraries - Third party packages

# Write a script to check if a file exists and print a message if it does

# import os

# filepath = "interview.md"

# if os.path.exists(filepath):
#     print(f"The file {filepath} exists. ")
# else:
#     print(f"The file {filepath} doesnt exist")


# list all files in a directory
# import os
# directory="./"

# for file_name in os.listdir(directory):
#     print(file_name)



# file_path="README.md"

# with open(file_path, "r") as file:
#     content=file.read()
#     print(content)


# import os
# directory_path="scripts"
# if not os.path.exists(directory_path):
#     os.makedirs(directory_path)
#     print(f"Directory {directory_path} is created successfully")
# else:
#     print(f"Directory {directory_path} already exists")


# import os
# directory_path='./'
# for file_name in os.listdir(directory_path):
#     if file_name.endswith(".log"):
#         file_path=os.path.join(directory_path, file_name)
#         os.remove(file_path)
#         print(f"Deleted {file_path}")


import subprocess

result = subprocess.run(["echo", "Hello, World"], capture_output=True, text=True)
print(result.stdout)  # Output: Hello, World!
