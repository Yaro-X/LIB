import os
vedio_list = []
start_dir = input("pls input the start dir: ")

def search(start_dir):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            ext = os.path.splitext(each_file)[1]

            if ext in [".mp4" , ".rmvb" , ".avi" , ".doc"]:
                vedio_list.append(os.getcwd() + os.sep + each_file +os.linesep)

        if os.path.isdir(each_file):
            search(each_file)
            os.chdir(os.pardir)

    return vedio_list



                
f = open("vedioList.txt" , "w")
f.writelines(search(start_dir))
f.close
