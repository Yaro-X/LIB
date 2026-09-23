import os
file_dict = {}
all_file = os.listdir("e:/Movie")

for each_file in all_file:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():
    print("%s[%d b]"%(each[0],each[1]))



    

        
            
        
