f = open("k:/999-/f.txt")

boy = []
girl = []
count =1

for each_line in f:
    if each_line[:3] != "===":

        (role,spoken_line) = each_line.split(":",1)

        if role == "小甲鱼":
            boy.append(spoken_line)

        if role == "小客服":
            girl.append(spoken_line)

    else:
        name_boy = "boy_" + str(count) + ".txt"
        file_boy = open(name_boy,"w")
        file_boy.writelines(boy)
        file_boy.close()

        name_girl = "girl_" + str(count) + ".txt"
        file_girl = open(name_girl,"w")
        file_girl.writelines(girl)
        file_girl.close()

        boy = []
        girl = []
        count += 1

name_boy = "boy_" + str(count) + ".txt"
file_boy = open(name_boy,"w")
file_boy.writelines(boy)
file_boy.close()

name_girl = "girl_" + str(count) + ".txt"
file_girl = open(name_girl,"w")
file_girl.writelines(girl)
file_girl.close()

f.close()
                                         
