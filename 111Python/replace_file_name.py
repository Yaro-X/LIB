import os
import re
import subprocess

current_dir = f'''G://MP3/T_to_mp3/to_be_convert'''

def list_files_basic():

    print(f"当前目录: {current_dir}\n")

    # 获取目录下所有条目
    items = os.listdir(current_dir)

    # 过滤出文件（排除目录）
    files = [item for item in items if os.path.isfile(os.path.join(current_dir, item))]

    print("文件列表:")
    for i, file_name in enumerate(files, 1):
        # print(f"{file_name}")
        rename_file(file_name)

def rename_file(self_filename):
    # print(self_filename)
    old_name = f'''{current_dir}/{self_filename}'''
    print(f'''当前显示old_name:{old_name}''')
    # regex = r'\(P(\d+)\.\s*(\d+)\.\s*([^)]+)\)'
    # regex = r'\(P\d+\.\s*\d+\s*-\s*(.+?)\)?-soConvert\.mp3$'
    # regex = r'\(P\d+\.\s*\d+\.\s*([^)]+)\)\.mp4$'
    regex = r'(.*).mp4' #直译
    match = re.search(regex, self_filename)
    if match:
        # print(match.group(1))
        new_name = f'''{current_dir}/{match.group(1)}.mp3'''
        print(f'''当前显示new_name:{new_name}''')

        ###convert to mp3
        convert_to_mp3(old_name, new_name)

        ###修改文件名
        # modify_file(old_name, new_name)
    # new_name = old_name.replace(f'''Hollow_Knight-Silksong''', f'''Divinity_Original''')
    # print(new_name)
    # os.rename(old_name, new_name)

def convert_to_mp3(self_oldname, self_newname):
    subprocess.run(['ffmpeg', '-i', self_oldname, '-vn', '-q:a', '0', self_newname])

def modify_file(self_oldname , self_newname):
    os.rename(self_oldname, self_newname)

if __name__ == "__main__":
    list_files_basic()
