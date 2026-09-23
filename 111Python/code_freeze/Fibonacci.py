'''
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。  
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。
'''
dic_fib ={0:0 , 1:1}

#吃橘子问题和 斐波那契数列 有相似
#故把 数列也列出来
def f11(self): #数列 方法1， 这个方法涉及大量重复计算，很慢不推荐
    if self <=2:
        return 1
    else:
        return f11(self -1) + f11(self -2)

def fib(self1): #数列 方法2，对比方法1，因为有字典记录计算过程，不需要重复计算，有就直接取数，没有才根据已有的计算，这样快很很恨多
    if self1 in dic_fib.keys():
        return dic_fib[self1]

    else:
        result = fib(self1-1) + fib(self1-2)
        dic_fib[self1] = result
        return result

def minDays(self1): #吃橘子问题
    if self1 in dic_fib.keys():
        return dic_fib[self1]

    else:
        min_day = min(self1 % 2 + minDays(self1 // 2) ,self1 % 3 + minDays(self1 // 3)) +1
        dic_fib[self1] = min_day
        return min_day

#print(f11(10))
print(fib(600))      
#print(minDays(101))    

'''
吃橘子的天数可以分为3个部分： 
（不能被2 or 3 整除时 要单独每天吃1个，这样要几天） + （当天吃 一半or 2/3） + （吃完剩下的要几天）
不能被2 or 3 整除时 要单独每天吃1个，这样要几天 -- 用 n%2 or n%3 取余数 表示
当天吃 一半or 2/3                            -- 这个要1天
吃完剩下的要几天                              --执行函数计算剩下的，相当于递归
'''