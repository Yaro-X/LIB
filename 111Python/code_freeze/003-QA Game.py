import random
identifyingcode = random.randint(000000,999999)
print(identifyingcode)

code = int(input('please input identifying code: '))

i=3

while code != identifyingcode:
    i = i-1
    if i > 0:
         print('you have '+ str(i) + ' chance')
         code = int(input('code is wrong,please input again:'))
    else:
        break

if i > 0:    
     print('suceed')
     print('end')
else:
    print('ban')
