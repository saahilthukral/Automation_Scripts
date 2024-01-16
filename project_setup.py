import os
import subprocess

# Get the path of the desktop directory
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Create projects directory inside desktop directory if it doesn't exist
projects_path = os.path.join(desktop_path, "projects")
if not os.path.exists(projects_path):
    os.makedirs(projects_path)

# Get the project name from the user
project_name = input("Enter the name of your project: ")

# Create the project directory inside the projects directory
project_path = os.path.join(projects_path, project_name)
if not os.path.exists(project_path):
    os.makedirs(project_path)

# Create start.py file in the project directory
start_py_path = os.path.join(project_path, "start.py")
with open(start_py_path, "w") as file:
    file.write("# This is the start file for your project")

# Create README.md file in the project directory
readme_md_path = os.path.join(project_path, "README.md")
with open(readme_md_path, "w") as file:
    file.write("# " + project_name)

# Initialize git in the project directory
subprocess.run(["git", "init"], cwd=project_path)

# Open the project directory in Visual Studio Code
subprocess.run(["code", project_path])

print(f"New project '{project_name}' created inside 'projects' directory.")