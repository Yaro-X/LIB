def mul(n):
    if n == 1:
        return 1
    else:
        return n * mul(n-1)

num = int(input("pls input num"))
res = mul(num)
print("%d的阶乘是%d"%(num , res))
    
