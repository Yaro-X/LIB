i3 = []
i4 = []
i5 = []
for i in range(100,99999):
    temp = i
    sum = 0
    a = len(str(temp))

    while temp:
        sum = (temp % 10) ** a +sum

        temp = temp//10

    if sum == i:
        if a ==3:
            i3.append(i)

        elif a ==4:
            i4.append(i)

        elif a ==5:
            i5.append(i)

print('三位数的自幂数为水仙花数，有' + str(len(i3)) +'个,分别是：',i3)
print('四位数的自幂数为四叶玫瑰数，有'+str(len(i4))+'个，分别是:',i4)
print('五位数的自幂数为五角星数，有'+str(len(i5))+'个，分别是：',i5)
        

