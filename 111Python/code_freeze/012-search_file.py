import os
star_dir = input("pls input the star path: ")
target = input("pls input the file name: ")

def search(star_dir,target):
    os.chdir(star_dir)
    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)

        if os.path.isdir(each_file):
            search(each_file,target)
            os.chdir(os.pardir)

search(star_dir,target)

