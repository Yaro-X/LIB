import threading , time ,os ,xlrd , re
from concurrent.futures import ThreadPoolExecutor as tp

p0 = "xxx"
cmd_list = []
pool = tp(10)

def loop_load(self_start , self_end):
    start_time1 = time.time()
    for i in range(self_start , self_end):
        val = worksheet.row_values(i)
        if len(val[1]) >0:
            print(val[1])
            time.sleep(0.1)
            os.system(val[0])
    end_time1 = time.time()    
    print(start_time1 - end_time1)

workbook = xlrd.open_workbook(p0)
worksheet = workbook.sheets()[0]
nrows = worksheet.nrows

how_many_threading = (nrows // 100)+1

t = [
    threading.Thread(target = loop_load , args=(1,101)),
    threading.Thread(target = loop_load , args=(101,201)),
    threading.Thread(target = loop_load , args=(201,301))
]








for each_t in t[0:how_many_threading]:
    each_t.start()


    #########
def task(self_cmd):
    print(self_cmd)
    time.sleep(0.1)
    os.system(self_cmd)

workbook = xlrd.open_workbook(p0)
worksheet = workbook.sheets()[0]
nrows = worksheet.nrows
start_time1 = time.time()
for i in range(1,nrows):
    val = worksheet.row_values(i)
    if len(val[1]) > 0:
        print(val[1])
        pool.submit(task,val[1])
pool.shutdom(True) #等所有线程跑完才执行下面的
end_time1 = time.time()
print(start_time1 - end_time1)