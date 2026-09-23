import os, xlrd, re, xlwt
import pandas as pd

country=[]
p0=""
workbook = xlrd.open_workbook(p0)
worksheet = workbook.sheets()[3]
nrows - worksheet.nrows
title = worksheet.row_values(0)
all_tb = []

for i in range(1,nrows):
    val = worksheet.row_values(i)
    country.append(val[2])
    all_tb.append(val)
country = list(set(country))

write_wb = xlwt.Workbook(encoding="UTF-8")    
for j in country:
    row=0
    write_ws = write_wb.add_sheet(j)
    for t in range(len(title)):
        write_ws.write(0,t,title[t])
        
    for each_tb in all_tb:
        if each_tb[2] == j:
            row += 1
            for col in range(len(each_tb)):
                print(row,col,each_tb[col])
                write_ws.write(row,col,each_tb[col])
write_wb.save("")                