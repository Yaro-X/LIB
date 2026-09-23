def narcissus():
    for i in range(100,99999):
        temp = i
        a = len(str(i))
        sum = 0

        while temp > 0:
            sum = (temp %10) ** a + sum
            temp = temp // 10

        if sum == i:
            print(i)

narcissus()
