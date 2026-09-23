# import os
# file_dict = {}
# all_file = os.listdir("e:/Movie")

# for each_file in all_file:
#     if os.path.isfile("e:/Movie/"+each_file):
#         file_size = os.path.getsize(each_file)
#         file_dict[each_file] = file_size

# for each in file_dict.items():
#     print("%s[%d b]"%(each[0],each[1]))

import os

def search_file(start_dir, target):
    os.chdir(start_dir)  # 切换当前工作目录

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)  # 使用os.sep使程序更标准
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
search_file(start_dir, target)
