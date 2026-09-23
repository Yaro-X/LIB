#def findstr(desstr,substr):
desstr = input('please input the desstr:')#文本文档，生成为str格式
substr = input('please input the substr:')#目标字符串,str
                                          #显示特定位置字符串的方法是从变量名后加[]和数字：desstr[1]
                                          #（从0开始数，0,1,2，...）

count = 0
length = len(desstr)                      #统计文本文档总字数（包括标点符号空格），从0开始数
if substr not in desstr:
    print('not found the target str')

else:
    for i in range(length):               #如果文本文档第i个的字符串 = 第一个目标字符串[0]
        if desstr[i] == substr[0]:
            #print('---i=',i)
            #print('desstr[i]:',desstr[i])
            #print('substr[1]:',substr[0])
            if desstr[i+1] == substr[1]:   #如果文本文档第i+1个的字符串 = 第二个目标字符串[1]
                #print('desstr[i+1]:',desstr[i+1])
                #print('substr[1]:',substr[1])
                count = count+1

    print('substr in desstr totaly %d times' % count)

#findstr(desstr,substr)


#you cannot improve your past,but you can improve your future .once times is wasted,life is wasted
