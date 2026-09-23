import os
import xlrd

path = "k://999-/精友2021年3月车型.xlsx"
p2 = "k://999-/111/"

workbook = xlrd.open_workbook(path)
worksheet = workbook.sheets()[1]

col1 = list(set(worksheet.col_values(colx =1)))
col2 = list(set(worksheet.col_values(colx =2)))

for dir1 in col1:
    os.makedirs(p2 + dir1)
    for dir2 in col2:
        os.makedirs(p2 + dir1 + "/" + dir2)
