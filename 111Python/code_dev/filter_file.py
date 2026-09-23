import os
path  = f'''G://onebizarre/silk song/'''

for root, dirs, files in os.walk(path):
    for each_file in files:
        # if '[01]' in
        # print(each_file)
        each_file_path = path+each_file
        print(each_file_path)
        # if '[01]' not in each_file_path:
            # print(each_file_path)
            # os.remove(each_file_path)
            # pass