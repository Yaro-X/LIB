import os , xlrd ,re
p0 ="x://xxx"

i_want - int()
cp_path={'radar4land-dev-0001':'radar51land-dev-0002'}

def cp_meta():
    copy_to = cp_path[val[10]]
    print(f'''gsutil cp gs//''')
    
if i_want ==0:
        workbook = xlrd.open_worbook(p0)
        worksheet = workbook.sheets()[1]
        nrows = worksheet.nrows
        for i in range(0,nrows):
            val = worksheet.row_values(i)
            
            if 'gs' in val[0]:
                file = re.findall(r'''gs://(.*?)/(.*)''',val[0])
                copy_to = cp_path[file[0][0]]
                print(f'''gsutil cp {val[0]} gs://{copy_to}/{file[0][1]}''')
                #print(f'''gsutil setmeta -h "x-goog-meta-*" gs://{copy_to}/{file[0][1]}''')
                
elif i_want ==9:
    workbook = xlrd.open_worbook(p0)
    worksheet = workbook.sheets()[0]
    nrows = worksheet.nrows
    for i in range(0,nrows):
        val = worksheet.row_values(i)
        if len(val[0]) > 0:
            if i ==1:
                print(f'''\'{val[0]}\'''')
            else:
                print(f''',\'{val[0]}\'''')
        else:
            continue