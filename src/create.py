#!/usr/bin/env python3
import sys, os, git
    
def create_files(dir_name):
    """[Creates files and directories]

    Args:
        dir_name ([str]): [The directory that is created]
    """
    
    # Attempts to create director, returns if it already exists
    try:
        os.mkdir(dir_name)
        print("Directory created: " + dir_name)
    except OSError as error: 
        print(error)
        return
    
    # Init new git repo
    repo = git.Repo.init(dir_name)
    print("Initalized git repo")
    
    # cd ./[dir_name]
    os.chdir(dir_name)
    
    # Add default directories
    os.mkdir("src")
    os.mkdir("resources")
    os.mkdir("test")
    print("Directories created: src, resources, test")
    
    # Create the .gitignore and README.md files
    if(os.path.exists("./" + dir_name + ".gitignore") == False):
        GIT_IGNORE = open(".gitignore", "x")
        print("Created: .gitignore")
        
    if (os.path.exists("./" + dir_name + ".README.md") == False):
        README = open("README.md", "x")
        print("Created: README.md")
    
    # Files to stage 
    repo.index.add([".gitignore", "README.md", "resources", "test", "src"])
    print("Staged files: " + ".gitignore", "README.md", "resources", "test", "src")
    
    # Initial commit 
    repo.index.commit('Initial commit.')
    print("Committed files.")
    
def main():
    """[Script main function]
    """
    
    # Check if they provide arguemnts
    if(len(sys.argv) < 2):
        print("Please specify the directory name.")
        return
    
    create_files(sys.argv[1])
        
# Calls main function
main()