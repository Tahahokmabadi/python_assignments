import os

# os.getcwd(): Get the current woeking directory
cwd = os.getcwd()
print("Current working directory:\n" , cwd)
print()

#os.path(path)
path = "C:/Users/Ati/Desktop/In-class projects (py)"
outpot_1 = os.path.basename(path) # returns the basename of the file from the given path
outpot_2 = os.path.dirname(path) # returns the directory name from the given path (except the path name)
print("file basename:", outpot_1)
print("directory name:", outpot_2)
print()

# os.mkdir(path) : Create a new directory
newdir = "newdir"
parent_dir = "C:/Users/Ati/Desktop/In-class projects (py)"
path = os.path.join(parent_dir, newdir)
os.mkdir(path)
print("New directory:\n" , path)
print()

# os.listdir() : Listing files and directories in the specified directory
path = "C:/Users/Ati/Desktop/In-class projects (py)"
dir_list = os.listdir(path)
print(f'files and directories in " {path} " :')
print(dir_list)
print()

# os.remove() : Used to remove a empty directory by the given path
file = "newdir"
location = "C:/Users/Ati/Desktop/In-class projects (py)/"
path = os.path.join(path, file)
os.rmdir(path)
print(f'Removing "{file}" ...')
