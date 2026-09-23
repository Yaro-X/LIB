import calendar as cd
year = int(input('请输入年：'))
month =int(input('请输入月：'))
day = int(input('请输入日：'))
last_day= cd.monthrange(year,month)[1]
if day == last_day:
    print(f'''{day}号是{year}年{month}月的最后一天''')
else:
    print(f'''{day}号不是{year}年{month}月的最后一天''')
