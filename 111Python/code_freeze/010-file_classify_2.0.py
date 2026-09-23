prime_num = []
for i in range(90000,99999):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime_num.append(i)

print(prime_num)
